
var macroName = document.getElementsByName('macro-name')[0];
var macroAttribute = document.getElementsByName('macro-attribute')[0];
var macroImg = document.getElementsByName('macro-img-gif')[0];
var macroCriticalRange = document.getElementsByName('macro-critical-range')[0];
var macroDamage = document.getElementsByName('macro-damage')[0];
var macroCritical = document.getElementsByName('macro-critical')[0];
var macroProficiency = document.getElementsByName('macro-pb')[0];
var macroAttkQtd = document.getElementsByName('macro-attk-qtd')[0];
var macroGlobalAttack = document.getElementsByName('macro-global-attk-mod')[0];
var macroGlobalDamage = document.getElementsByName('macro-global-dmg-mod')[0];
var macroEffectType = document.getElementsByName('macro-effect-type')[0];
var macroEffectColor = document.getElementsByName('macro-effect-color')[0];

var macroPreviewName = document.querySelector('#macro-preview-name');
var macroPreviewImg = document.querySelector('#macro-preview-img');

var macroOutput = document.getElementById('macro-output-textarea');
// Update the preview name
macroName.addEventListener('input', function(){
	if(macroName.value != ''){
		macroPreviewName.innerHTML = macroName.value;
	}
})

// Update the preview image/gif 
macroImg.addEventListener('input', function(){
	if(macroImg.value != ''){
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


// Theme mode
var themeMode = document.getElementsByName('theme-mode')[0];
var macroInfo = document.getElementById('macro-info');
var macroPreview = document.getElementById('macro-preview');
var themeModeIcon = document.getElementById('theme-mode-icon');
var macroPreviewSquare = document.getElementById('macro-preview-square');
var macroPreviewRow1 = document.getElementsByClassName('macro-preview-row-1')[0];
var macroPreviewRow2 = document.getElementsByClassName('macro-preview-row-2')[0];
var macroPreviewRowRoll = document.getElementsByClassName('macro-preview-row-roll');
var macroPreviewTitle = document.getElementsByClassName('frame-title-preview')[0];
themeMode.addEventListener('change', function(){
	if(themeMode.checked == true){
		themeModeIcon.src = 'icons/moon_icon.png';
		macroInfo.style = "background: linear-gradient(-45deg, #560033, #2d1336);";
		macroPreview.style = "background-color: #353535";
		macroPreviewSquare.style = "background-color: #1f1f1f;";
		macroPreviewRow2.style = "background-color: transparent; color: white;";
		macroPreviewRow1.style = "background-color: #353535; color: white;";
		for (var i = macroPreviewRowRoll.length - 1; i >= 0; i--) {
			macroPreviewRowRoll[i].style = "background-color: #702082;";
		}
		macroPreviewTitle.style = "color: white;";
	} else{
		themeModeIcon.src = 'icons/sun_icon.png';
		macroInfo.style = "background: linear-gradient(-45deg, #ea018c, #772b90);";
		macroPreview.style = "background-color: white";
		macroPreviewSquare.style = "background-color: transparent;";
		macroPreviewRow1.style = "background-color: #ccc; color: black;";
		macroPreviewRow2.style = "background-color: white; color: black;";
		for (var i = macroPreviewRowRoll.length - 1; i >= 0; i--) {
			macroPreviewRowRoll[i].style = "background-color: #fef68e;";
		}
		macroPreviewTitle.style = "color: #702082;";
	}
})

// Generate de Macro
macro = "";
function genMacro(){
	macroName = document.getElementsByName('macro-name')[0];
	macroAttribute = document.getElementsByName('macro-attribute')[0];
	macroImg = document.getElementsByName('macro-img-gif')[0];
	macroCriticalRange = document.getElementsByName('macro-critical-range')[0];
	macroDamage = document.getElementsByName('macro-damage')[0];
	macroCritical = document.getElementsByName('macro-critical')[0];
	macroProficiency = document.getElementsByName('macro-pb')[0];
	macroAttkQtd = document.getElementsByName('macro-attk-qtd')[0];
	macroGlobalAttack = document.getElementsByName('macro-global-attk-mod')[0];
	macroGlobalDamage = document.getElementsByName('macro-global-dmg-mod')[0];
	macroEffectType = document.getElementsByName('macro-effect-type')[0];
	macroEffectColor = document.getElementsByName('macro-effect-color')[0];

	macro = "&{template:default}{{name=" + macroName.value + "}}";
	var attribute = "";
	var proficiency = "";
	var globalDamage = "";
	var globalAttack = ""
	var effectType = "";
	var effectColor = "";
	var effect = "";

	if(macroImg.value != ""){
		macro += "{{[Image](" + macroImg.value + ")}}";
	}

	if(macroAttribute.selectedIndex == 1){
		attribute = "+@{strength_mod}";
	} else if(macroAttribute.selectedIndex == 2){
		attribute = "+@{dexterity_mod}";
	} else if(macroAttribute.selectedIndex == 3){
		attribute = "+@{constitution_mod}";
	} else if(macroAttribute.selectedIndex == 4){
		attribute = "+@{intelligence_mod}";
	} else if(macroAttribute.selectedIndex == 5){
		attribute = "+@{wisdom_mod}";
	} else if(macroAttribute.selectedIndex == 6){
		attribute = "+@{charisma_mod}";
	}

	if(macroProficiency.checked == true){
		proficiency = "+@{pb}";
	}

	if(macroGlobalAttack.checked == true){
		globalAttack = '+@{global_attack_mod}';
	}

	if(macroGlobalDamage.checked == true){
		globalDamage = '+@{global_damage_mod_roll}';
	}

	if(macroAttkQtd.value == 1){
		macro += "{{ Attack: [[1d20cs>" + macroCriticalRange.value + attribute + proficiency + "(" + globalAttack + ")]] Advantage: [[1d20cs>" + macroCriticalRange.value +  attribute + proficiency + "(" + globalAttack + ")]]}}{{ Damage: [[" + macroDamage.value + attribute + globalDamage  + "]] Critical: [[" + macroCritical.value + attribute + globalDamage  + "]]}}"; 
	} else if(macroAttkQtd.value > 1){
		for(let i = 1; i <= macroAttkQtd.value; i++){
			macro += "{{ " + i + "° Attack: [[1d20cs>" + macroCriticalRange.value +  attribute + proficiency + "(" + globalAttack + ")]] Advantage: [[1d20cs>" + macroCriticalRange.value +  attribute + proficiency + "(" + globalAttack + ")]]}}{{ " + i + "° Damage: [[" + macroDamage.value + attribute + globalDamage + "]] Critical: [[" + macroCritical.value + attribute + globalDamage + "]]}}"; 
		}
	}

	macroOutput.innerHTML = macro;

	if(macroEffectType.selectedIndex != 0){
		if(macroEffectColor.selectedIndex != 0){
			switch(macroEffectType.selectedIndex){
			case 1:
				effectType = "\n/fx beam-";
				break;
			case 2:
				effectType = "\n/fx bomb-";
				break;
			case 3:
				effectType = "\n/fx breath-";
				break;
			case 4:
				effectType = "\n/fx bubbling-";
				break;
			case 5:
				effectType = "\n/fx burn-";
				break;
			case 6:
				effectType = "\n/fx explode-";
				break;
			case 7:
				effectType = "\n/fx glow-";
			case 8:
				effectType = "\n/fx missile-";
				break;
			case 9:
				effectType = "\n/fx nova-";
			case 10:
				effectType = "\n/fx splatter-";
				break;
			}

			switch(macroEffectColor.selectedIndex){
			case 1:
				effectColor = "acid";
				break;
			case 2:
				effectColor = "blodd";
				break;
			case 3:
				effectColor = "charm";
				break;
			case 4:
				effectColor = "death";
				break;
			case 5:
				effectColor = "fire";
				break;
			case 6:
				effectColor = "frost";
				break;
			case 7:
				effectColor = "holy";
				break;
			case 8:
				effectColor = "magic";
				break;
			case 9:
				effectColor = "slime";
				break;
			case 10:
				effectColor = "smoke";
				break;
			case 11:
				effectColor = "water";
				break;
			}
			effect = effectType + effectColor;
			macro += effect + " @{target|Source|token_id} @{target|Target|token_id}";
			macroOutput.innerHTML = macro;
		} else{
			macroOutput.innerHTML = "Select an effect color!";
		}
	}
}

function copyMacro(){
	navigator.clipboard.writeText(macro);
	alert("Macro copied to clipboard!");
}