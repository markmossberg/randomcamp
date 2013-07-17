function process(){

	// get input and verify
	var input = $("input").value;
	if (!isNum(input)){
		alert("Input must be a number, give it another try.");
		clearForm();
		return
	}
	input = Math.floor(input);

	// the good stuff
	wordList = randWords();
	console.log(wordList);
};


function randWords(){
	wordnikUrl = "http://api.wordnik.com/v4/words.json/randomWords?limit=12&maxLength=8&api_key=32549059d8e5389e4432f22bd79186407ce3eca763cd3564b";

	var request = new XMLHttpRequest();
	request.open("GET", wordnikUrl, false);
	request.send();
	wordnikResp = request.responseText;

	var randWords = new Array();
	var wordnikResponse= JSON.parse(wordnikResp);
	for (var i = 0; i < 12; i++){
		randWords[i] = wordnikResponse[i].word;
	}

	return randWords;
};

function clearForm(){
	$("input").value = "";
};

function isNum(variable){
	return !isNaN(parseInt(variable));
};

function $(id){
	return document.getElementById(id);
};
