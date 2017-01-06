
// The following statement does not belong to any method. Hence,
// it is a global variable that can be accessed by any methods in this
// webpage.
// This global variable is an array that will be used to store objects
// of the drawing information.
var drawings = [];

function searchInputChange() {
    var queryText = document.getElementById("searchInput").value;
    console.log(queryText);
    if (queryText) { // this is truthy
        $.ajax({url: "/searchDrawing/?query=" + queryText,
            success: function(result){
                console.log(result);
                if (result === "Failed") {
                    return;
                }
                var DrawingIDList = document.getElementById("DrawingIDList");
                DrawingIDList.innerHTML = "";
                drawings = [];
                var jsonResult = JSON.parse(result);
                for (var i = 0; i < jsonResult.rtnList.length; i++) {
                    var item = jsonResult.rtnList[i];
                    drawings.push(item);
                    var newOption = document.createElement('option');
                    newOption.text = item.DrawingID;
                    DrawingIDList.appendChild(newOption);
                }
                drawingInfoListChange();

            }
        });
    } else {
        document.getElementById("DrawingIDList").innerHTML = "";
    }

}

















// The following prototype is defined to store drawing information.
function Drawing(id,bn,year,con,floor, shop)
{
    this.DrawingID = id;
    this.BuildingName = bn;
    this.ConstructedYear = year;
    this.Contractor = con;
    this.Floor = floor;
    this.Shop = shop;
}



// The following statement is a method that create initial drawing objects
// and add them to the array drawings.
function initDrawings()
{
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function()
    {
        if(xhttp.readyState == 4 && xhttp.status == 200)
        {
            var data = xhttp.responseText;
            var drawingStrings = data.split(";");

            for(var i=0;i<drawingStrings.length;i++)
            {
                var drawingString = drawingStrings[i];
                var attributeStrings = drawingString.split(",");
                var newDrawing = new Drawing(attributeStrings[0], attributeStrings[1], attributeStrings[2], attributeStrings[3], attributeStrings[4], attributeStrings[5]);
                drawings.push(newDrawing);

            }
            alert("A total of "+drawings.length+" drawings are added to the array.");
        }

    };

    xhttp.open("GET", "/loadDrawings/",true);
    xhttp.send();
}

// The following method load drawing data to create drawing objects,
// and then add the ID of the objects to the dropdown list, with the ID
// DrawingIDList.
function addDrawingInfoToList()
{
    if(drawings.length==0)
    {
        alert("Please load the initial drawings to the array first.");
        return;
    }
    // First, we need to get a reference of the HTML tag DrawingIDList.
    var HTMLDrawingList = document.getElementById("DrawingIDList");

    // Before adding all drawings to the list, the list needs to be
    // emptied so that no repeated item will show.
    // One simple way to empty a list is to set innerHTML of the list
    // to an empty string, which means that there is no option tag.
    HTMLDrawingList.innerHTML = "";

    // Now we can started to add new items to the list.
    for(var i=0;i<drawings.length;i++)
    {
        // In order to add an item to the list, we need to create a
        // tag <option>, which defines an item in a <select> tag.
        var newOption = document.createElement("option");
        // Then provide the innerText to this option.
        newOption.innerText = drawings[i].DrawingID;

        // Every option also has an attribute named value. This attribute
        // can be specified as any values. Here we use the index of the item
        // as the value for each option. But this example does not use the value
        // of options.
        newOption.value = i;

        HTMLDrawingList.appendChild(newOption);
    }

    alert("A total of "+drawings.length+" drawings are added to the HTML list.");

}

// The following event is triggered by the change of selection in the drawing
// information list.
function drawingInfoListChange()
{
    console.log("Call drawingInfoListChange");
    var HTMLDrawingList = document.getElementById("DrawingIDList");

    // The selectedIndex attribute belongs to any <select> tag.
    // It represents the current index of the selected item.
    var drawingIndex = HTMLDrawingList.selectedIndex;

    // Since the items in the drawinginfoList is the same order
    // as the drawings list, the index of the selected item also represents
    // the index of the drawing item in the array.
    var selectedDrawing = drawings[drawingIndex];
    // Now we can use this selected object of the drawing to update the
    // drawing information.
    var buildingNameText = document.getElementById("buildingNameInput");
    buildingNameText.value = selectedDrawing.BuildingName;

    document.getElementById("constructedYearInput").value = selectedDrawing.ConstructedYear;
    document.getElementById("contractorInput").value = selectedDrawing.Contractor;
    document.getElementById("floorInput").value = selectedDrawing.Floor;

    if(selectedDrawing.Shop != undefined)
        document.getElementById("shopInput").value = selectedDrawing.Shop;
    else
        document.getElementById("shopInput").value = "";

}

// The following function asks for a new ID that user will input for the drawing.
// It will check whether there is any drawing that has the same ID. If yes, it will
// provide a message saying that this ID exist. Otherwise, it will add a new drawing object.
// with information in the input boxes to the array and reload the ID to the drawinglist.
function addDrawing()
{
    // Ask the user to enter an ID for the new drawing.
    var newID = prompt("Please enter a new ID for the drawing");
    if(newID==undefined)
    {
        alert("Please enter the new ID.");
        return;
    }

    // Check whether this new ID exists in the drawing list.
    for(var i=0;i<drawings.length;i++)
    {
        if(drawings[i].DrawingID == newID)
        {
            alert("This ID exists.");
            return;
        }
    }

    // If this ID does not exist, using the information from the current text boxes
    // to create the new drawing object.
    var buildingNameText = document.getElementById("buildingNameInput").value;
    var constructedYearText = document.getElementById("constructedYearInput").value;
    var contractorText = document.getElementById("contractorInput").value;
    var floorText = document.getElementById("floorInput").value;
    var shopText = document.getElementById("shopInput").value;

    var newDrawing = new Drawing(newID, buildingNameText,constructedYearText,
        contractorText,floorText);

    newDrawing.Shop = shopText;

    // Add teh new drawing object to the list.
    drawings.push(newDrawing);

    // Reload the HTML drawing list tag.
    addDrawingInfoToList();

    // Send data to database.
     var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function()
    {
        if(xhttp.readyState == 4 && xhttp.status == 200)
        {
            console.log(xhttp.responseText);
        }
    };

    var sendParameters = "?DrawingID="+newID+"&BuildingName="+buildingNameText
    +"&ConstructedYear="+constructedYearText+"&Contractor="+contractorText+"&Floor="+
            floorText+"&Shop="+shopText;


    xhttp.open("GET", "/addDrawing/"+sendParameters,true);
    xhttp.send();
}

// The following function will update the drawing that is currently selected in the 
// HTML drawing list (the <select> tag), using the information in the text boxes.
function updateDrawing()
{
    // First, we need to get the selected index in the HTML drawing list.
    var HTMLDrawingList = document.getElementById("DrawingIDList");
    // The selectedIndex attribute belongs to any <select> tag.
    // It represents the current index of the selected item.
    var drawingIndex = HTMLDrawingList.selectedIndex;

    // Since the items in the drawinginfoList is the same order
    // as the drawings list, the index of the selected item also represents
    // the index of the drawing item in the array.
    var selectedDrawing = drawings[drawingIndex];

    selectedDrawing.BuildingName = document.getElementById("buildingNameInput").value;
    selectedDrawing.ConstructedYear = document.getElementById("constructedYearInput").value;
    selectedDrawing.Contractor = document.getElementById("contractorInput").value;
    selectedDrawing.Floor = document.getElementById("floorInput").value;
    selectedDrawing.Shop = document.getElementById("shopInput").value;

    // After updating the attributes, set the object back to the same location in the drawing array.
    drawings[drawingIndex] = selectedDrawing;


    // Send data to database.
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function()
    {
        if(xhttp.readyState == 4 && xhttp.status == 200)
        {
            console.log(xhttp.responseText);
        }
    };

    var sendParameters = "?DrawingID="+selectedDrawing.DrawingID+"&BuildingName="+selectedDrawing.BuildingName
    +"&ConstructedYear="+selectedDrawing.ConstructedYear+"&Contractor="+selectedDrawing.Contractor+"&Floor="+
            selectedDrawing.Floor+"&Shop="+selectedDrawing.Shop;


    xhttp.open("GET", "/updateDrawing/"+sendParameters,true);
    xhttp.send();
}

function deleteDrawing()
{
    var HTMLDrawingList = document.getElementById("DrawingIDList");

    // The selectedIndex attribute belongs to any <select> tag.
    // It represents the current index of the selected item.
    var drawingIndex = HTMLDrawingList.selectedIndex;
    // Delete this item from the array drawings. The splice method can remove the item in an array.
    drawings.splice(drawingIndex,1);

    // After removing this item, reload the data.
    addDrawingInfoToList();

    drawingInfoListChange();

}
