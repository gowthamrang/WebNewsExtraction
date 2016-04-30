// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

var min = 1;
var max = 5;
var current = min;
var version_number = '/V3'

var client = new Dropbox.Client({token: "ciUPn3BjnEAAAAAAAAAAD7Qysck2bqyvlyUlreDGynoGxHRyUHN7B6phGdmvdbur"});

var newarray = {}
//  //newarray['http://www.chicoer.com/breakingnews/ci_24157652/woman-shot-by-chico-officers-identified'] = 'f865'
//  newarray['http://boston.cbslocal.com/2013/08/07/boston-police-officer-shot-by-suspect-in-dorchester/'] = 'f98'
//  newarray['http://www.nydailynews.com/new-york/brooklyn/kimani-gray-remembered-school-principal-heartfelt-letter-article-1.1290668'] = 'f161'
 
//  newarray['http://pensacolapolice.com/08222012-2/'] = 'f54'
//  newarray['http://m.savannahnow.com/news/2009-10-13/savannah-man-idd-passenger-killed-high-speed-pursuit#gsc.tab=1'] = 'f866'

//  newarray['http://www.stltoday.com/news/local/crime-and-courts/man-identified-in-fatal-shooting-by-police-in-eureka/article_356fc7c8-9577-5e30-a624-e742bbe747b4.html'] = 'f575'
//  newarray['http://www.dispatch.com/content/stories/local/2013/05/16/shootout-officers-identified.html'] = 'f551'
 
//  //newarray['http://www.northfulton.com/Articles-TOP-STORIES-c-2013-04-16-198337.114126-sub-Suspect-dead-after-chase-shooting.html'] = 'f497'

//  newarray['http://www.mysanantonio.com/news/local_news/article/Three-Rivers-police-kill-man-during-scuffle-4445847.php'] = 'f495'
//  newarray['http://www.reviewjournal.com/news/deadly-force/incident/42'] = 'f412'
//  newarray['http://www.sfgate.com/bayarea/article/Family-disputes-Oakland-police-version-of-fatal-2501304.php'] = 'f384'
//  newarray['http://www.sfgate.com/news/article/Fourth-Oakland-officer-involved-in-Saturday-s-3167588.php'] = 'f338'
//  //newarray['http://www.mymotherlode.com/news/local/1871597/No-Charges-In-Deputy-Shooting.html'] = 'f273' 

// newarray['http://www.latimes.com/world/middleeast/la-fg-yemen-blast-20150107-story.html'] = 'g10249'  	
// newarray['http://www.mirror.co.uk/news/billingshurst-double-death-mum-dad-4875740']	 = 'g6511'  
// //newarray['http://www.bradfordtoday.com/2015/01/07/al-qaeda-hit-dozens-die-in-yemen-police-academy-blast/']	= 'g10112'  
// newarray['http://www.spyghana.com/ghanas-nsd-participation-compulsory-kofi-boakye/'] ='g9000'  
// //newarray['http://www.ktvu.com/story/27713316/fremont-police-kill-rampaging-sick-coyote'] = 'g6444'  	
// newarray['http://townhall.com/columnists/anncoulter/2015/01/07/dying-for-a-cigarette-in-new-york-n1939997/page/full'] = 'g13113'  	
// newarray['http://www.theadvertiser.com/story/news/local/2015/01/10/new-iberia-man-killed-in-broussard-crash/21548825/'] = 'g12615'  	
// newarray['http://www.foxnews.com/world/2014/12/30/canada-police-edmonton-man-with-lengthy-criminal-record-kills-8-people-before/'] = 'g8910'
// newarray['http://fox43.com/2015/01/13/police-protestors-plan-die-in-at-farm-show/'] = 'g13249'
// //newarray['http://www.nationalreview.com/article/396071/i-am-not-charlie-hebdo-maggie-gallagher']	= 'g11432'
// //newarray['https://au.news.yahoo.com/thewest/national/a/25783241/stabbing-suspect-in-melbourne-siege/']	= 'g2128'
// //newarray['http://time.com/3644273/horrid-holiday-travel-weather/'] = 'g4955'

// //newarray['http://www.bradenton.com/2015/01/05/5564216/savannah-police-seek-truck-after.html'] = 'g9371'
// //newarray['http://www.bradenton.com/2014/12/21/5543349/2-cops-ambushed-fatally-shot-in.html'] = 'g4251'
// newarray['http://ksn.com/2015/01/09/police-official-charlie-hebdo-suspects-dead-hostage-freed/']  = 	'g11776'
// newarray['http://www.nwherald.com/2015/01/03/police-waukegan-man-kills-woman-in-front-of-her-daughter/aove021/'] = 'g8836'
// newarray['http://sputniknews.com/europe/20150111/1016754353.html'] = 'g12434'
// newarray['https://www.ijreview.com/2015/01/229959-cops-heartbroken-reaction-shoot-kill-man/'] = 'g11908'
// newarray['http://www.bradenton.com/2014/12/31/5556586/an-unreal-feeling-ohalloran-family.html'] = 	'g7693'
// newarray['http://www.nbc15.com/home/headlines/Police-2-car-crash-in-Oconto-Falls-kills-both-drivers-288250751.html'] = 'g13016'

// newarray['http://www.inquisitr.com/1695005/cop-killings-police-officer-shot-killed-tarpon-springs-florida/'] = 'g4790'
// //newarray['http://www.ynetnews.com/articles/0,7340,L-4605883,00.html'] = 'g4385'
// newarray['http://news.yahoo.com/guyana-police-arrest-man-suspected-killing-3-161116024.html'] = 'g6519'
// newarray['http://zeenews.india.com/news/world/police-kill-six-attackers-in-chinas-xinjiang-govt_1528750.html'] = 'g12781'
// //newarray['http://weku.fm/post/videos-ray-rice-eric-garner-among-biggest-media-moments-2014'] = 'g5330'
// //newarray['http://www.montrealgazette.com/News/canada/Ashby+Rinelle+Harper+challenge+Perry+Bellegarde+Stephen/10654692/story.html'] = 'g2447'


// newarray['http://kfgo.com/news/articles/2014/dec/23/exhausted-sierra-leone-medics-battle-ebola-in-the-red-zone/'] = 'g5464'
// newarray['http://abcnews.go.com/US/man-killed-police-shooting-ferguson-missouri/story?id=27807891'] = 'g5621'
// newarray['http://www.ohio.com/news/local/barberton-funeral-directors-recruited-to-help-keep-unused-prescription-meds-out-of-wrong-hands-1.549782'] = 'g1670'
// newarray['http://www.westernjournalism.com/sheriff-joe-predicts-new-york-police-deaths-just-first-many/'] = 'g5198'
// //newarray['http://www.utsandiego.com/news/2014/dec/27/afghan-police-lead-insurgent-fight-at-high-cost/'] = 'g6678'
// newarray['http://www.deathandtaxesmag.com/232645/man-fails-drunk-driving-test-after-telling-police-hes-going-to-kill-them-all/'] = 'g2787'
// newarray['http://www.fox8live.com/story/27784375/citizens-battle-over-smoking-ban-at-no-council-meeting'] = 'g10468'
// //newarray['http://www.wspa.com/story/27765377/mauldin-police-officer-dies-in-fatal-motorcycle-wreck'] = 'g9545'
// newarray['http://www.independent.co.uk/news/world/europe/paris-attacks-moment-armed-police-storm-kosher-supermarket-shooting-gunman-and-freeing-hostages-9969936.html'] = 'g12516'

// newarray['http://abcnews.go.com/International/wireStory/turkish-police-chief-detained-journalists-killing-29238542'] ='115298'
// newarray['http://www.kcra.com/news/police-man-woman-killed-in-shooting-at-fresno-medical-office/32113704'] ='128436'
// newarray['http://www.heraldsun.com.au/news/law-order/police-seek-man-after-woman-filmed-in-toilet-at-fitzroy-bar/story-fni0fee2-1227220198008'] ='110698'
// newarray['http://www.independent.ie/world-news/europe/putin-turns-screw-with-threat-to-cut-off-gas-supply-unless-kiev-pays-first-31026288.html '] ='115838'
// newarray['http://www.kfvs12.com/story/27988269/police-3-year-old-dies-after-being-hit-by-truck-in-parking-lot'] ='105516'

// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-05_86798.html'] = '86798'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-05_86464.html'] = '86464'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-06_86970.html'] = '86970'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-06_88085.html'] = '88085'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-06_88326.html'] = '88326'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-07_94197.html'] = '94197'

// //unable to see clearly
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-07_89428.html'] = '89428'

// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-07_91627.html'] = '91627'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-09_103060.html'] = '103060'

// //Not in list
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-09_96197.html'] = '96197'

// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-09_103855.html'] = '103855'
// //Not good scrap
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-10_115298.html'] = '115298'

// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-10_128436.html'] = '128436'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-10_110698.html'] = '110698'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-16_130824.html'] = '130824'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-16_130964.html'] = '130964'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-16_130645.html'] = '130645'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-17_131256.html'] = '131256'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-17_131266.html'] = '131266'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-17_131298.html'] = '131298'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-23_1970.html'] = '1970'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-23_363.html'] = '363'

// //Obituary
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-04-23_3492.html'] = '3492'

// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-25_135241.html'] = '135241'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-25_134743.html'] = '134743'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-25_133343.html'] = '133343'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-26_135822.html'] = '135822'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-26_135731.html'] = '135731'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-26_135700.html'] = '135700'

// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-27_136026.html'] = '136026'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-27_135962.html'] = '135962'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-27_135928.html'] = '135928'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-28_136224.html'] = '136224'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-28_136135.html'] = '136135'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-28_136182.html'] = '136182'

// //WTF >
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-29_136257.html'] = '136257'

// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-29_136258.html'] = '136258'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-29_136281.html'] = '136281'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-30_136429.html'] = '136429'
// newarray['http://hobbes.cs.umass.edu/~ranga/scrap/2015-05-30_136470.html'] = '136470'

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