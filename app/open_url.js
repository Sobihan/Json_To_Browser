function open_url() {
    my_electron = require("electron");
    missing_cp = false;
    var data = document.getElementById("data").value;

    try {
        var my_json = JSON.parse(data);
    }
    catch (e) {
        if (e instanceof SyntaxError) {
            return false;
        }
    }
    length = my_json["samples"]["length"];
    if (!my_json.samples[0].parsed_cps.cp) {
        missing_cp = true;
    }
    for (let index = 0; index < length; index = index + 1) {
        if (missing_cp == true) {
            my_electron.shell.openExternal(my_json["samples"][index]["cp"]["url"]); 
        } else {
            my_electron.shell.openExternal(my_json["samples"][index]["parsed_cps"]["cp"]["url"]);
        }
    }
    document.getElementById("data").value = "";
    return true;
}

function call_open_url() {

    var my_label =  document.querySelector('#label');
    my_data = document.querySelector("#data");
    var is_soso_algo = document.querySelector('.switch > input').checked;

    if (is_soso_algo == true) {
        algo_soso();
    } else {
    if (open_url() == false) {
        my_label.textContent = "Try again !";
        my_data.classList.add("null-data");
    } else {
        my_label.textContent = "Paste your JSON here !";
        my_data.classList.remove("null-data");
    }
    return true;
    }

}

function handle_go_btn_events(event) {
    if (event.keyCode == 13) {
        call_open_url();
        return false;
    }
}

function algo_soso() {
    var my_label =  document.querySelector('#label');
    var my_json = document.getElementById("data").value.split('"');
    const length = my_json.length;
    var urls = [];
    var tmp = null;

    for (let index = 0; index < length; index = index + 1) {
        if (my_json[index] == 'url') {
            tmp = my_json[index + 2];
            if (urls.includes(tmp) == false) {
                urls.push(tmp);
                my_electron.shell.openExternal(tmp);
            }
        }
    }
    my_label.textContent = "Paste your JSON here !";
    return true;
}