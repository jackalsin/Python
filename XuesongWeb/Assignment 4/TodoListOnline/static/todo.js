var globalTasks = [];


addTask = function () {
    var idToAdd = prompt("Please provide a new ID for the current task");

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var data = xhttp.responseText;
            if (data == "true") { // exist
                alert("Duplicated ID.\nPlease enter another one");

            } else if (data == "false") {
                // send to
                alert("Not a duplicated ID");
                var descriptionInput = document.getElementById("descriptionInput").value;
                var dueDateInput = document.getElementById("dueDateInput").value;
                var statusInput = document.getElementById("statusInput").value;
                console.log("Status input = " + statusInput);
                var xhttpToAddTask = new XMLHttpRequest();
                xhttpToAddTask.onreadystatechange = function () {
                    console.log("Send to add task: " + xhttpToAddTask.responseText);
                };

                xhttpToAddTask.open("GET", "/addTask/?TaskId=" + idToAdd + "&desInput="+descriptionInput+"&dueDateInput="+dueDateInput+"&statusInput="+statusInput);
                xhttpToAddTask.send();
            } else {
                console.log("Wrong return value: " + data);
            }
        }
    };
    xhttp.open("GET", "/checkID/?TaskId="+ idToAdd, true);
    xhttp.send();
};

loadTasks = function () {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var allJsonObject = xhttp.responseText;
            var taskSelect = document.getElementById("taskSelect");
            var taskListReceived = JSON.parse(allJsonObject);
            console.log(taskListReceived);
            for (var i = 0; i < taskListReceived.length; i++) {
                var curJSON = taskListReceived[i];
                // copy
                globalTasks.push(curJSON);
                var curOpt = document.createElement("option");
                curOpt.text = curJSON['TaskID'];
                taskSelect.appendChild(curOpt);
                document.getElementById("descriptionInput").value = curJSON['Description'];
                document.getElementById("dueDateInput").value = curJSON['DueDate'];
                document.getElementById("statusInput").checked = curJSON['Status'] ;
            }
        }
    };
    xhttp.open("GET", "/loadTasks/");
    xhttp.send();
};

onchangeHandler = function () {
    var selectedValue = document.getElementById("taskSelect").value;
    console.log(selectedValue);
    for (var i = 0; i < globalTasks.length; i++) {
        var child = globalTasks[i];
        if (selectedValue === child['TaskID']) {
            document.getElementById("descriptionInput").value = child['Description'];
            document.getElementById("dueDateInput").value = child['DueDate'];
            document.getElementById("statusInput").checked = child['Status'] ;
        }
    }

};