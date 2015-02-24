//sMenu hace todo lo necesario para ordenar el menu, y sin JQuery
//JQuery es mas rapido :P
function sMenu()
{
    var MenuBar = document.getElementById('MenuBar');
	var ContentWrapper = document.getElementById('ContentWrapper');
	var state = MenuBar.style.width;

	var width = window.innerWidth;

	if(!(state.match("45%")))
	{
		MenuBar.style.opacity = 1;
		MenuBar.style.width = '45%';
		ContentWrapper.style.width = '55%';
		ContentWrapper.style.marginLeft = '45%';
	}
	else
	{
		MenuBar.style.zIndex = "0";
		MenuBar.style.opacity = 0;
		MenuBar.style.width = '0%';
		ContentWrapper.style.width = '100%';
		ContentWrapper.style.marginLeft = '0%';
	}

	if(width > 1024)
	{
		MenuBar.style.opacity = 1;
		MenuBar.style.width = '20%';
		ContentWrapper.style.width = '80%';
		ContentWrapper.style.marginLeft = '20%';
	}
}

//Esta funcion ajusta el icono de menu

function adjust()
{
	var width = window.innerWidth;

	if(width > 1024)
	{
		MenuBar.style.opacity = 1;
		MenuBar.style.width = '20%';
		ContentWrapper.style.width = '80%';
		ContentWrapper.style.marginLeft = '20%';
	}
	else
	{
		MenuBar.style.zIndex = "0";
		MenuBar.style.opacity = 0;
		MenuBar.style.width = '0%';
		ContentWrapper.style.width = '100%';
		ContentWrapper.style.marginLeft = '0%';
	}
}

//Esta funcion ajusta los iFrames si utilizas videos externos de YouTube

function resVideo()
{
	frame = document.getElementById("video");
	frameWidth = frame.offsetWidth;
	frame.style.height = (frameWidth * 0.56) + "px";
}
