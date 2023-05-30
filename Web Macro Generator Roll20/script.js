
var macroName = document.getElementsByName('macro-name')[0];
var macroImg = document.getElementsByName('macro-img-gif')[0];
var macroAttkQtd = document.getElementsByName('macro-attk-qtd')[0];
var macroAttribute = document.getElementsByName('macro-attribute')[0];


var macroPreviewName = document.querySelector('#macro-preview-name');
var macroPreviewImg = document.querySelector('#macro-preview-img');

// Update the preview name
macroName.addEventListener('input', function(){
	if(macroName.value == ''){
		macroPreviewName.innerHTML = "Attack";
	} else{
		macroPreviewName.innerHTML = macroName.value;
	}
})

// Update the preview image/gif 
macroImg.addEventListener('input', function(){
	if(macroImg.value == ''){
		macroPreviewImg.src = "";
	} else{
		macroPreviewImg.src = macroImg.value;
	}
})

// Update the number of attaks in preview
var square = document.getElementById('macro-preview-square');
var row = document.getElementsByClassName('complete-attack-row')[0];
macroAttkQtd.addEventListener('input', function(){
	let attkQtd = macroAttkQtd.value;
	let currentAttksQtd = document.getElementsByClassName('complete-attack-row').length;
	let difference = attkQtd - currentAttksQtd;
	console.log(difference);
	if(difference > 0){
		let newRow = document.createElement('div');
		newRow.className = 'complete-attack-row';
		newRow.innerHTML = row.innerHTML
		square.appendChild(newRow);
	}
	if (difference < 0) {
		var currentAttks = square.querySelectorAll('.complete-attack-row');
		for(let i = currentAttksQtd - 1; i >= attkQtd; i--){
			square.removeChild(currentAttks[i]);
		}
	}
});

