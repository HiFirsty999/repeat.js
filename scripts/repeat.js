let Display = document.getElementById("LoopOutput");
let TextIn = document.getElementById("Text");
let RC = document.getElementById("RC");
let SB = document.getElementById("SB");

function Loop(TextInput, RepeatCount) {
    let Result = "";

    for (let x = 1; x <= RepeatCount; x++) {
        Result += `${x}. ${TextInput}\n`;
    };

    return Result;
};

function ShowResult() {
    let TextInValue = TextIn.value
    let RCValue = parseInt(RC.value)

    Display.innerText = `${Loop(TextInValue, RCValue)}`;
};

SB.addEventListener("click", ShowResult);