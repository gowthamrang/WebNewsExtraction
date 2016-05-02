
  var port = chrome.runtime.connect({name: "knockknock"});

/* SO*/
//Question 
// 1. Does next node in DOM tree = next node in render ?
function nextNode(node) {
    if (node.hasChildNodes()) {
        return node.firstChild;
    } else {
        while (node && !node.nextSibling) {
            node = node.parentNode;
        }
        if (!node) {
            return null;
        }
        return node.nextSibling;
    }
}

function getRangeSelectedNodes(range) {
    var node = range.startContainer;
    var endNode = range.endContainer;

    // Special case for a range that is contained within a single node
    if (node == endNode) {
        return [node];
    }

    // Iterate nodes until we hit the end container
    var rangeNodes = [];
    while (node && node != endNode) {
        rangeNodes.push( node = nextNode(node) );
    }

    // Add partially selected nodes at the start of the range
    node = range.startContainer;
    while (node && node != range.commonAncestorContainer) {
        rangeNodes.unshift(node);
        node = node.parentNode;
    }

    return rangeNodes;
}

function getSelectedNodes() {
    if (window.getSelection) {
        var sel = window.getSelection();        
            return getRangeSelectedNodes(sel.getRangeAt(0));
    }
    return [];
}


function getPathTo(element) {    
    if (element.parentNode == null) return ''

    var ix= 0;
    var tx = 0
    var siblings= element.parentNode.childNodes;
    for (var i= 0; i<siblings.length; i++) {
        var sibling= siblings[i];        
        if (sibling===element &&  element.tagName) return getPathTo(element.parentNode) + '/' + element.tagName.toLowerCase() + '[' + (ix + 1) + ']';
        if (sibling===element) return getPathTo(element.parentNode) + '/text()' + '[' + (tx + 1) + ']';
        
        if (sibling.nodeType===Node.ELEMENT_NODE && sibling.tagName === element.tagName) {
            ix++;
        }else{
            if (sibling.nodeType == Node.TEXT_NODE) tx++;
        }
    }
}

/* SO http://stackoverflow.com/questions/7781963/js-get-array-of-all-selected-nodes-in-contenteditable-div*/

function similarity(text1,text2){
    return Math.abs(text1.split(" ").length - text2.split(" ").length)/(text1.split(" ").length+1) <0.2
}


port.onMessage.addListener(function(msg) {
  if (msg.state == "Get me selected text"){
    var groundtruth = []
    var nodelist = getSelectedNodes()
    var res = ""
    var overlap = window.getSelection().toString()
    overlap.replace(/\r\n|\n/, ' ') //\n is a special character for us
    var selected_text = ""
    for (var i = 0; i <= nodelist.length - 1; i++) {
        if (nodelist[i].nodeType == Node.TEXT_NODE){
            var path = getPathTo(nodelist[i])
            var headings = document.evaluate(getPathTo(nodelist[i]), document, null, XPathResult.ANY_TYPE, null); 
            var thisHeading = headings.iterateNext(); 
            var selection_in_node = ""
            while (thisHeading) {
                console.log(thisHeading)
              selection_in_node += thisHeading.nodeValue; //UTF-16 
              thisHeading = headings.iterateNext();
            }
            console.log(nodelist[i].nodeValue)
            console.log([path,selection_in_node])
            selection_in_node.replace(/\r\n|\n/, ' ') //\n is a special character for us
            groundtruth.push([path,selection_in_node])
            res += selection_in_node
        }
    }
    console.log(res)
    console.log(overlap)
    console.log(similarity(res,overlap ) )
    port.postMessage({state:"Resp",selectedtext: [groundtruth, overlap], path:msg.path, url: document.URL}); 
}
});
