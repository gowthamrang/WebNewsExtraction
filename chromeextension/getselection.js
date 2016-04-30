
  var port = chrome.runtime.connect({name: "knockknock"});


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
        if (!sel.isCollapsed) {
            return getRangeSelectedNodes(sel.getRangeAt(0));
        }
    }
    return [];
}



port.onMessage.addListener(function(msg) {

  if (msg.state == "Get me selected text"){
	port.postMessage({state:"Resp",selectedtext: window.getSelection().toString(), path:msg.path, url: document.URL}); 
	array = getSelectedNodes()
	console.log('kko')
	for (var i = array.length - 1; i >= 0; i--) {
		console.log(array[i].getparent())
	};
 }
}


);



