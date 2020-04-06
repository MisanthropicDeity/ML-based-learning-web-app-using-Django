window.addEventListener('load', ()=>{
	//console.log("Hello");
	const canvas =document.querySelector("#canvas");
	const context = canvas.getContext("2d");

	//Resizing
	
	// canvas.height = window.innerHeight;
	// canvas.width = window.innerWidth;
	canvas.width = 500;
	canvas.height = 500;
	 //context.fillRect(50,50 ,200, 200);
	let painting = false;
	context.fillStyle = "white";
	context.fillRect(0, 0, canvas.width, canvas.height);

	function startPosition(){
		console.log("1")
		painting = true;
		//draw(e);
	}
	function finishedPosition(){
		console.log("2")
		painting = false;
		context.beginPath();
	}
	function draw(e){
		console.log("3")
		if(!painting) return;
		context.lineWidth = 40;
		context.lineCap = "round";

		context.lineTo(e.pageX,e.pageY-40);
		console.log(e.pageX,e.pageY)
		context.stroke();
		context.beginPath();
		context.moveTo(e.pageX,e.pageY-40)
	}

	//Event Listeners
	canvas.addEventListener('mousedown',startPosition);
	canvas.addEventListener('mouseup',finishedPosition);
	canvas.addEventListener('mousemove',draw);


	document.getElementById('clear').addEventListener('click', function() {
        context.clearRect(0, 0, canvas.width, canvas.height);
      }, false);

	var dataURL = canvas.toDataURL();
	//document.getElementById('canvasImg').src = dataURL;
})


//window.addEventListener('resize,')