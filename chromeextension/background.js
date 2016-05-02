var min = 1;
var max = 5;
var current = min;
var version_number = '/VPublic'

var client = new Dropbox.Client({token: ""});

var newarray = {}
newarray['http://www.dailythanthi.com/News/India/2016/03/14212414/Mallya-case-ED-writes-to-banks-multiple-probe-agencies.vpf'] = 'abcd'

function purge(path){
	client.writeFile(path, '', function(error, stat) {
		if (error) {
  			alert(error)
		}else{
		}
	});

}

chrome.browserAction.onClicked.addListener(function (tab){
	console.log(tab.url)
	url = tab.url
	temp = url.split('/')
	if temp.length>4 && temp[1] == 'hobbes.cs.umass.edu' && temp[2]=='~ranga' && temp[3]=='scrap':
		alert('GOT THE LINK')
	else{
		return
	}
	temp = temp[temp.length-1].split('_')
	id = temp[temp.length-1].split('.')[0]
	console.log(id)

	return

	path = version_number+'/Title/'+newarray[url]+'.groundtruth'
	purge(path)
	path = version_number+'/Body/'+newarray[url]+'.groundtruth'
	purge(path)
	path = version_number+'/Authors/'+newarray[url]+'.groundtruth'
	purge(path)
	path = version_number+'/Publish_date/'+newarray[url]+'.groundtruth'
	purge(path)
	
	
});

function fillTitle() {
	connectionport.postMessage({state:'Get me selected text', path:version_number+'/Title/'});
  chrome.browserAction.setIcon({path:"icon" + 5 + ".png"});
  current++;

  if (current > max)
    current = min;
}

function fillBody() {
	connectionport.postMessage({state:'Get me selected text', path:version_number+'/Body/'});
  chrome.browserAction.setIcon({path:"icon" + 5 + ".png"});
  current++;

  if (current > max)
    current = min;
}


function fillDate() {
	connectionport.postMessage({state:'Get me selected text', path:version_number+'/Publish_date/'});
  chrome.browserAction.setIcon({path:"icon" + 5 + ".png"});
  current++;

  if (current > max)
    current = min;
}


function fillAuthor() {
	connectionport.postMessage({state:'Get me selected text', path:version_number+'/Authors/'});
  chrome.browserAction.setIcon({path:"icon" + 5 + ".png"});
  current++;

  if (current > max)
    current = min;
}


//chrome.browserAction.onClicked.addListener(updateIcon);
chrome.contextMenus.create({
 title: "Body",
 contexts:["selection"],  // ContextType
 onclick: fillBody
  // A callback function
});

chrome.contextMenus.create({
 title: "Title",
 contexts:["selection"],  // ContextType
 onclick: fillTitle // A callback function
});


chrome.contextMenus.create({
 title: "Publish_date",
 contexts:["selection"],  // ContextType
 onclick: fillDate // A callback function
});


chrome.contextMenus.create({
 title: "Authors",
 contexts:["selection"],  // ContextType
 onclick: fillAuthor // A callback function
});

//updateIcon();

var connectionport = null

  


chrome.runtime.onConnect.addListener(function(port){
	console.assert(port.name == "knockknock");
	connectionport = port
	port.onMessage.addListener(function(msg){
		console.log(msg.url)
		console.log(newarray)

	    if (msg.state == "Resp"){
	    	
	    	if (newarray[msg.url]){
	    		path = msg.path+newarray[msg.url]+'.groundtruth'
	    		console.log(msg.selectedtext)
	    		console.log(path)
	    		//It it exists get the 
	    		var contents = ''
	    		client.readFile(path, {arrayBuffer: false}, function(error, cnts){
	    			
	    			if (!error && cnts != undefined) {
	    				
	    				console.log(cnts)
	    				context = cnts
	    			}
				    
				    //console.log(decoded); 
				    //Doesnt matter if it exists
		    		client.writeFile(path, contents+' '+msg.selectedtext, function(error, stat) {
			    		if (error) {
			      			console.log(error)
			      			alert(error)
			    		}else{
			    			//console.log(stat)
			    			//console.log('Written')
			    		}
		    		});
				});
	    		
	    		//log file writes and time to check for overwrite etc., ?

	    	}else{
	    		alert('URL not in news list!: Not saving data')
	    	}
	    }	
	    	
    });
});