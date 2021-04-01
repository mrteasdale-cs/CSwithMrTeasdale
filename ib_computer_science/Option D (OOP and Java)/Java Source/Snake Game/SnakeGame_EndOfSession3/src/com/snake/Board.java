package com.snake;

import com.snake.templates.AbstractBoard;
import com.snake.templates.AbstractSnake;
import com.snake.ui.BoardUI;
import com.snake.ui.ScoreBar;
import javax.swing.Timer;

/**
 * This is a class representing the game board for our Snake game.
 */
public class Board extends AbstractBoard {

   private BoardUI ui = null;
   private int rows;
   private int cols;
   private Snake snake;
   // This variable will hold the actual grid behind the game board!
   // Notice it is made up of 'Cell' objects, a custom class that we
   // will be extending!
   private Cell[][] grid;
   private Timer timer;
   private TimerListener timerListener;

   public Board(int cellSize, int rows, int cols) {
      this.rows = rows;
      this.cols = cols;

      // Add code here for Task 2 to set up the grid array
      grid = new Cell[rows][cols];

      for (int row = 0; row < rows; row++) {
         for (int col = 0; col < cols; col++) {
            grid[row][col] = new Cell(cellSize, row, col);
         }
      }

      this.snake = new Snake(this);
   }

   /**
    * This method is called when the Snake game starts. We will implement this
    * later
    */
   public void start() {
      // Place the Snake on the board
      snake.place();

      // Create and start the timer object - used to make the game tick
      timerListener = new TimerListener(snake);
      timer = new Timer(250, timerListener);

      timer.start();

      ScoreBar.getInstance().setStatus("Game started!");

      placeFood();
   }

   /**
    * When this method is first called, it will create a new BoardUI object, and
    * every time after that it will use the already created object.
    *
    * @return BoardUI object.
    */
   public BoardUI getBoardUI() {
      if (ui == null) {
         ui = new BoardUI(this, rows, cols);
      }
      return ui;
   }

   /**
    * Get the Cell object located at the given row and column
    */
   public Cell getCell(int row, int col) {
      return grid[row][col];
   }

   /**
    * Get the Snake object
    */
   public Snake getSnake() {
      return snake;
   }

   /**
    * Start or stop the timer
    */
   public void setTimer(boolean state) {
      if (state)
         timer.start();
      else
         timer.stop();
   }

   public void placeFood() {
      boolean emptySpaceFound = false;

      int row = -1;
      int col = -1;
      while (!emptySpaceFound) {
         row = (int) (Math.random() * rows);
         col = (int) (Math.random() * cols);

         emptySpaceFound = getCell(row, col).getType() == CellType.EMPTY;
      }

      getCell(row, col).setType(CellType.FOOD);
   }
}