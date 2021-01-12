const general = document.getElementById("general");
const fun = document.getElementById("fun");
const giveaway = document.getElementById("giveaway");
const mod = document.getElementById("mod");
const music = document.getElementById("music");

function hideall(){
	general.setAttribute("hidden", "");
	fun.setAttribute("hidden", "");
	giveaway.setAttribute("hidden", "");
	mod.setAttribute("hidden", "");
	music.setAttribute("hidden", "");
}

function generalCommands(){
	hideall();
	general.removeAttribute("hidden");
}

function musicCommands(){
	hideall();
	music.removeAttribute("hidden");
}


function funCommands(){
	hideall();
	fun.removeAttribute("hidden");
}

function giveawayCommands(){
	hideall();
	giveaway.removeAttribute("hidden");
}

function infoCommands(){
	hideall();
	info.removeAttribute("hidden");
}

function modCommands(){
	hideall();
	mod.removeAttribute("hidden");
}

function randomCommands(){
	hideall();
	random.removeAttribute("hidden");
}

window.onload = function(){
	generalCommands();
}