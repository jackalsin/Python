/**
 * Created by jacka on 11/13/2016.
 */

/* Main game logic is here. */
function Game() {
  // constants
  // todo: probably change the canvas size will be an easy way to go.
  this.HIGHT = 640;
  this.WIDTH = 800;
  const COLS = 7;
  const ROWS = 6;
  this.CELL_SIZE = 75;
  this.CIRCLE_RADIUS = 25;
  this.X_MARGIN = (this.WIDTH - this.CELL_SIZE * (COLS - 1)) / 2;
  const Y_MARGIN = (this.HIGHT - this.CELL_SIZE * (ROWS - 1)) / 2;

  const PLAYER_ID = 1;
  const OTHER_ID = -1;

  this.BOARD_COLOR = "#BBBBBB";
  this.PLAYER_COLOR = "#FF88FF";
  this.OTHER_COLOR = "#22FFCC";

  const CONNECT_NUMBER = 4;

  // variables
  this.map = [];
  this.isPaused = false;
  this.hasWinner = false;
  /* how many steps has been placed, including computer and player. */
  this.move = 0;
  this.hasInited = false;

  this.initOnce = function () {
    if(this.hasInited) {
      return false;
    }

    var that = this;
    this.canvas = $("#main")[0];
    this.context = this.canvas.getContext('2d');
    // init map 0 is empty, 1 is Filled.
    // according to WIki The most commonly used Connect Four board size is 7 columns × 6 rows
    this.canvas.addEventListener("click", function (e) {
      // todo: don't know how to do it.
      // this.parent().onclick(this.parent().canvas, e);
      that.onclick(that.canvas, e);
    });
        this.hasInited = true;
  };

  // reset all states to the initial state.
  this.clear = function () {
    this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
  };

  this.init = function () {
    // variables
    this.map = [];
    this.isPaused = false;
    this.hasWinner = false;
    /* how many steps has been placed, including computer and player. */
    this.move = 0;
    for (var i = 0; i < ROWS; i++) {
      var curRow = [];
      for (var j = 0; j < COLS; j++) {
        curRow.push(0);
      }
      this.map[i] = curRow;
    }

    this.initOnce();
    this.clear();
    this.drawBoard();
  };

  /* Check if there is a winner or not or it's already a draw. */
  this.checkHasWinner = function () {
    for (var i = 0; i < ROWS; i++) {
      for (var j = 0; j < COLS; j++) {
        var rightCounter = 0;
        var downCounter = 0;
        var rightDownCounter = 0;
        var rightUpCounter = 0;
        for (var k = 0; k < 4; k++) {
          if (j + k < COLS) {
            rightCounter += this.map[i][j + k];
          }
          if (i + k < ROWS) {
            downCounter += this.map[i + k][j];
          }
          if (j + k < COLS && i + k < ROWS) {
            rightDownCounter += this.map[i + k][j + k];
          }
          if (i - k >= 0 && j + k < COLS) {
            rightUpCounter += this.map[i - k][j + k];
          }
        } // end of k loop
        if (Math.abs(rightCounter) === 4) {
          this.win(rightCounter);
        }
        if (Math.abs(downCounter) === 4) {
          this.win(downCounter);
        }
        if (Math.abs(rightDownCounter) === 4) {
          this.win(rightDownCounter);
        }
        if (Math.abs(rightUpCounter) === 4) {
          this.win(rightUpCounter);
        }
      }
    }

    if (this.move === 42 && !this.hasWinner) {
      this.win(0);
    }
  };

  /* Winning process function. */
  this.win = function (winner) {
    this.hasWinner = true;
    var rect = this.canvas.getBoundingClientRect();
    if (winner === 0) {
      showWinningMsg(rect, this.context, "This is a draw");
    } else if (winner > 0) {
      showWinningMsg(rect, this.context, "You win, click to restart");
    } else {
      showWinningMsg(rect, this.context, "You lose, click to restart");
    }
  };

  function showWinningMsg(rect, context, msg) {
    context.save();
    context.font = "30px Arial";
    context.fillText(msg, rect.left, rect.top + Y_MARGIN/16);
    context.restore()
  }



  /* Define a function to draw the board. */
  this.drawBoard = function () {
    this.context.save();
    this.context.fillStyle = this.BOARD_COLOR;
    this.context.beginPath();
    for (var i = 0; i < ROWS; i++) {
      for (var j = 0; j < COLS; j++) {
        this.context.arc(
            this.CELL_SIZE * j + this.X_MARGIN, // center x
            this.CELL_SIZE * i + Y_MARGIN, // center y
            this.CIRCLE_RADIUS,
            0, // start angle
            2 * Math.PI // end angle
        );

        this.context.rect(
            this.CELL_SIZE * (j + 0.5) + this.X_MARGIN,
            this.CELL_SIZE * (i - 0.5) + Y_MARGIN,
            -this.CELL_SIZE, // use minus to do the trick
            this.CELL_SIZE
        );
      }
    }
    this.context.fill();
    this.context.restore();

  };

  // ------------ event controller -------------
  /* To determine if the button is on the board. */
  this.isOnBoard = function (relativeX, relativeY) {
    var rect = this.canvas.getBoundingClientRect();
    return relativeX >= 0 && relativeX <= innerWidth &&
            relativeY >= 0 && relativeY <= rect.height;
  };

  this.getColumnToFill = function (relativeX) {
    return parseInt(relativeX / this.CELL_SIZE, 10);
  };

  this.playerTurn = function () {
    return this.move % 2 > 0 ? PLAYER_ID : OTHER_ID;
  };

  /* The get most possible win place to win */
  function getMaxWin(map, dir) {
    var dx = dir[0];
    var dy = dir[1];



    var maxStateMap = [];
    var mostDangerousMap = [];
    for (var i = 0; i < map.length; i++) {
      var curRow = map[i];
      var maxRow = [];
      var dangerRow = [];
      for (var j = 0; j < curRow.length; j++) {
        var maxStateCounter = 0;
        var mostDangerousCounter = 0;
        var dangerDone = false;
        var maxDone = false;
        for (var k = 0; k < CONNECT_NUMBER; k++) {
          var x = i - k * dx;
          var y = j - k * dy;
          if (!maxDone) {
            if (x >= 0 && x < ROWS && y >= 0 && y < COLS && map[x][y] == PLAYER_ID) {
              maxStateCounter++;
            } else{
              maxRow.push(maxStateCounter);
              maxDone = true;
            }
          }
          if (!dangerDone) {
            if (x >= 0 && x < ROWS && y >= 0 && y < COLS && map[x][y] == PLAYER_ID) {
              mostDangerousCounter++;
            } else{
              dangerRow.push(mostDangerousCounter);
              dangerDone = true;
            }
          }
        } // end of k loop
      }
      maxStateMap.push(maxRow);
      mostDangerousMap.push(dangerRow);
    } // end of i loop

    // strategy
    function getMaxValueAndCord(map) {
      var dangerousRow = -1;
      var dangerousCol = -1;
      var dangerousVal = -1;
      for (var i = 0; i < map.length; i++) {
        var curRow = map[i];
        for (var j = 0; j < curRow.length; j++) {
          if (map[i][j] >= dangerousVal) {
            dangerousCol = j;
            dangerousRow = i;
            dangerousVal = map[i][j];
          }
        }
      }
      return [dangerousVal, dangerousRow, dangerousCol];
    }
    /* val, row, col*/
    var dangerVals = getMaxValueAndCord(mostDangerousMap);
    var maxVals = getMaxValueAndCord(maxStateMap);
    var rtnCol;
    if (dangerVals[0] >= 2) {
       rtnCol = (dangerVals[2] + 1) < COLS ? (dangerVals[2] + 1) : 0;
      return [dangerVals[0],rtnCol];
    } else {
      rtnCol = (maxVals[2] + 1) < COLS ? (maxVals[2] + 1) : 0;
      return [maxVals[0],rtnCol];
    }
  }

  this.ai = function () {
    var upMax = getMaxWin(this.map, [1,0]);
    var rightMax = getMaxWin(this.map, [0, 1]);
    var upRightMax = getMaxWin(this.map, [1, 1]);
    var downRightMax = getMaxWin(this.map, [-1,1]);
    var candidates = [upMax, rightMax, upRightMax, downRightMax];
    var colToFill = 0;
    var maxPriority = 0;
    for (var i = 0; i < candidates.length; i++) {
      var candidate = candidates[i]; //priority,
      if (maxPriority <= candidate[0]) {
        maxPriority = candidate[0];
        colToFill = candidate[1];
      }
    }
    this.playMove(colToFill, OTHER_ID);
    this.isPaused = false;
    this.move++;
  };

  this.action = function(columnToFill) {
    if (this.isPaused || this.hasWinner || this.map[0][columnToFill] != 0) {
      return 0;
    }
    this.playMove(columnToFill, PLAYER_ID);
    this.isPaused = true;
    this.move++;
    return 1;
  };

  this.playMove = function (columnToFill, id) {
    var rowToFill = -1;
    for (var i = ROWS - 1; i >= 0; i--) {
      if (this.map[i][columnToFill] == 0) {
        this.map[i][columnToFill] = id;
        rowToFill = i;
        break;
      }
    }
    // todo: debug info

    console.log("^^^^^^^^^^^^^^^^^^^^^^^^^^^");
    print2DArray(this.map);
    console.log("^^^^^^^^^^^^^^^^^^^^^^^^^^^");

    var color = this.playerTurn() == PLAYER_ID ? this.PLAYER_COLOR : this.OTHER_COLOR;
    this.drawCircle(rowToFill, columnToFill, color);
    this.checkHasWinner();
  };


  this.drawCircle = function (row, col, color) {
    var coordinator = this.indexToCoordination(row, col);

    this.context.save();
    this.context.fillStyle = color;
    this.context.beginPath();
    this.context.arc(coordinator[0], coordinator[1], this.CIRCLE_RADIUS, 0, Math.PI * 2);
    this.context.fill();
    this.context.restore();

  };
  /* Row Col to canvas coordination */
  this.indexToCoordination = function (row, col) {
    var y = (row) * this.CELL_SIZE + Y_MARGIN;
    var x = (col) * this.CELL_SIZE + this.X_MARGIN;
    return [x, y];
  };
  
  
  
  /* onclick handler, must return a boolean value to indicate if it's going to bubble */
  this.onclick = function (canvas, e) {
    if (this.hasWinner) {
      this.init();
      return false;
    }
    var rect = this.canvas.getBoundingClientRect();

    var relativeX = e.clientX - rect.left - this.X_MARGIN + 0.5 * this.CELL_SIZE;
    var relativeY = e.clientY - rect.top - Y_MARGIN + 0.5 * this.CELL_SIZE;
    if (!this.isOnBoard(relativeX, relativeY)) {
      return false;
    }
    var colToFill = this.getColumnToFill(relativeX);
    this.action(colToFill);
    if (!this.hasWinner) {
      this.ai();
    }
  };

  this.init();

  // -------- debug function
  function print2DArray (nestedArray) {
    for (var i = 0; i < nestedArray.length; i++) {
      var child = nestedArray[i];
      console.log(child);
    }
  }
}


/* Start the game when the document ready */
$(document).ready(function () {
  this.game = new Game();
});