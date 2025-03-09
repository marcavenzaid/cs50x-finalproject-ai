// Send an AJAX request to the "/stop_ongoing_speech" URL using fetch.
// Which will call a python function to stop the ongoing speech.
function stop_ongoing_speech() {
    fetch("/stop_ongoing_speech").then(function(response) {
        // do nothing other than send an AJAX request to the "/stop_ongoing_speech" URL using fetch.
    }).catch(function(error) {
        console.log("Error fetching /stop_ongoing_speech:", error);
    });
}

/**
 * Automatically adjusts the height of the text area to show all text inside it.
 */
function text_area_auto_grow() {
    textarea = document.querySelector("#inputMessage");
    textarea.addEventListener("input", autoResize, false);

    function autoResize() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    }
}
text_area_auto_grow();

// Pressing Enter submits form, and Shift+Enter adds a new line
document.getElementById("inputMessage").addEventListener("keypress", e => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();

        e.currentTarget.closest("form").submit();
    }
});

// document.querySelector("#questionMark").addEventListener("click", function(e) {
//     e.preventDefault();
//     document.getElementById("thought").innerText = "�̶̡͚̬̘̲͖̪̺̥̘̫̙̥̪̥͓̼̟̖̉̑̽̍̓̓̿̈́̆̌̐͊̃̆̕͜�̵⃥̸̨̡̡̛̛̜̪͖̱̠̗̘̯̗̖̻̭̲̟̹̩̼͎̳̬̹͇̙̩͉͍̖̙̳̳̳̯̄̌̈́͊͑́͛̒͛̓̆̂̌̊̀̿͌͌͋̓͒̓͛͒̿͠ͅͅ�̵̰̝̘̞̊̐͊̏͘͜ͅ�̶̸̷̧̨̨̧̧̢̨̳͇̠̻͔̗̜̘̳̠̥̯̱̬̜̟̯͙͈̭̙̠̩̲͕̰̫̯͇̗̪̺̼̞̹͔̪͓͍͎̙͕̏̂͋̓͛̈́̊̀̏̏̂́̑̃͋̈́̔́̐͑̑̑̏́̏́̈̚̕͝͝�̷̧̨̠̠̮̲͎̯̫͇͎͚̦̮͔͎́̑͂̔̋̽͒̏͋̇̀̉͒͒̂͊͒́̅̋͊͊̄̓͑̍̈́̾̌͘͘ͅ�̸⃥̷̧̧͚̫͎͚̠̟̝̲̲̦̪̞͈͎̣͙͎̳̺͔͉̗̥̗̤͆̓̍͌̈͆̄͑̐͗̽͌̌̃͋̋͒͆̏̓́̅̌͊̔̀͋̇̏̉̎̀̀͘͘͜͝͝͝�̶̻̯͚͎̟̈́̔̈͂̿͊́͆̔͛́͗̍̎̍̓͋̒̍̚̚͝͠�̵̸̴̨̛̛̭̤̲̪̝͔͈̪̩̫͎̮͖̭͖̫̞͙̠͉͇̫́̈̄̏͒̄͒̇̉̐̍̂͌́̎̓̀̈́͗̐͌̐͐͗̈́̉͋͆͒͌͆͗̇͐̈́̽̋͒̋̉́̑̋̀̂̐̃̌͋̌̋́̓̈́̉̍̒̍͘̕̕͘͘͜͜͜͜͝͠͝͠�̸̨̨̢̛̼͕̯̣̜̥̪̥̞͈̝̝͔̯̘͍͇͙͚͎̰͎͇̱̣͇̲̤̄̓̎̋͑͛̄̉̐͊̈͗̋̓̂̽̄͐͘̚͜�̶⃥̷̡̪̟͍͉̜̬̺̩̥̺̤̖̞̮̲͓̬̝͚̫̦͎̱̱̰̖̳̀̅́͐̈̓̔̉̑̍́̂̊̍͆͗̈́͆̋̒͘̚͜͜͝͝ͅ�̶̨̨̧̨̮̤͎̗̦̝̜̻͙̺̪̮̥̤̞̦̣̩͕͓̝̮̽͗̈́̐͐̐͜�̵̸̶̨̨̛̟͍̩̩͚̬̝̰͎͉̼̪͍͓̤̥̱̪̩̤̠̟̣͈̩̗̘̳̺͕͇̟̩͎̥̻̙̠̦͑͗̔́̃̀́̽̒̿̿͌͌͗͗͒̽͐͂̏̊̒͋̈̄͛͌̆̓̽̊̎̾͜͠͠�̴̞̍͐̀͆̄͆͗̍̄̒͝ͅ�̷⃥̴̢̢̛̜̣̘̖͙̳̺̳̱̝̬͉̦̤͖͓̩̝̼̪͇͇̗̥̥̞̪̐͊́̐̌̊́͐̋́̽̀͆͐̋̇͌̎͛͒͊̄̀́̋̓͜͜ͅ�̶̲̯́̀̒̾̀̎̾̽͒͒̄͌̒͑̐̄̓͝͝�̷̸̴̧̡̡̧͔̯̘̻͉̺̯̺̺̙͔͎͙̜̝͇̼̞̣͇͚̙͚̠̻͉̼̮͖̦̼̮̺̮̦͕̗̜͍͙̻͔͓̬̺̤͉͚̤̬̥̱̈́͛̎͂͗̆́̅̆̐̏̎̓̃̏̎̄̏̍͗͒̐̇̀͛̈͆̒͒͆͂̇͐͛͛̓͊̈́̇͛̂͘̚͜͠ͅ�̶̛͇̻̞͖̊͂̐͑͑̆͊͊̑̔͛̀́́̀̑̑̌̾̒̿́͂̔̔͒̎̿̆́̇̚̚͜͝͠�̶⃥̴̢̧̧̧̛̠̬͉͙͓͖͎͔͓̘̬̣̮̺̪̖͓̟̦̥͔̥̱̻͋́̾̔́͂̊̔̑́́̈́̄̈̒́̽̊̈̏̀͒̓̆͊̾̊̿͛̿̓͌͛̌̽̈́͘͘̕̕͜͠͝�̵̨̲͕̮͚͕̘͙̳̟͙̻͉̺̯̫̀̒̑͠͠�̶̸̷̢̢̧̢̲̩̗̱̦̩̝̜̥̠͙̼̹͇̘̠̝͎̻̪̬̹͇͔͎̯̜̥̲̻͖͎̣̘̹̻̖̬̭͍̙͈̮̬͙̤̘̼̘̍̂̎̊̏̇̈́͊̅̎̉͑̅̉͗͛̿́̈́͌̿͜ͅͅ�̵̦͈̯̣̤̜͊̉͌͗͋͂͊̏̓̽̿͘͘͝�̶⃥̶̢̢̧̧͕̭̖̦̯̫̠̝̟̖̬̳̮̼͎̝͍̯̹͉̯͓̯̦͖͖̳͍̯̦̥̞͓̌͂͂̓̍̎̔̀̒͊̓͊́͋̈̍̽͗̎̒̃͊͐̅̌̚͝͝͠͝ͅ�̸̢̢̜̘̲̙͈͇̤̔̐̽͋̓̐̔̈͌̍̌́͌͘͜͠�̴̸̷̢̢̛͙̹̦̭̭̼̫̠͔̭͓̫̥̩̜̘̖̥͈͔͇͍̲̺̯̰͓̠̗͙͇͎̗̹͎̞̘͈͙̯̞̘̩̇̐̒́͆͐̀͂̈́̂́͛̇̉̓̑͑̈́̀̆͐̈̅̊̉̌͌̈́̔͒̌̂̆̽̀̆͛̕͝͝ͅ";
// });
