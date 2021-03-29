package com.snake.ui;

import com.snake.Board;
import java.awt.BorderLayout;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class SnakeUI extends JFrame {

   private static final long serialVersionUID = 1L;
   // CELL_SIZE is the size of the side of each cell, in pixels
   private static final int CELL_SIZE = 15;
   private final Board board;

   public SnakeUI() {
      // This is the number of rows, and the number of cols in our grid
      int rows = 20;
      int cols = 40;

      // Create the ScoreBar, and place it at the bottom of the UI
      ScoreBar scorebar = ScoreBar.getInstance();
      add(scorebar, BorderLayout.SOUTH);

      // Create the board object, and use it to return the BoardUI
      board = new Board(CELL_SIZE, rows, cols);
      BoardUI boardUI = board.getBoardUI();
      add(boardUI);

      // These values are used to set the size of the window
      int boardWidth = (cols * CELL_SIZE) + (CELL_SIZE / 2) - 1;
      int boardHeight = (rows * CELL_SIZE) + (CELL_SIZE / 2) + 50;

      // Here we set the title and size of the window
      setTitle("Snake Game"); // TODO Change to your own title
      setSize(boardWidth, boardHeight);

      // This tells the program to exit when the red 'X' in the top right
      // corner is clicked
      setDefaultCloseOperation(EXIT_ON_CLOSE);

      // This makes the window appear in the middle, and stops you from
      // resizing the window
      setLocationRelativeTo(null);
      setResizable(false);

      // This means that the window can have focus (and we can move the
      // Snake with the keyboard
      setFocusable(true);
   }

   /**
    * Return the board object, we need this method so it can be called from the
    * main method below
    */
   public Board getBoard() {
      return board;
   }

   /**
    * This is the main method that the program execution starts from. This
    * basically sets up the UI and makes it visible.
    */
   public static void main(String[] args) {
      SwingUtilities.invokeLater(new Runnable() {

         @Override
         public void run() {
            SnakeUI ui = new SnakeUI();
            ui.setVisible(true);
            ui.getBoard().start();
         }
      });
   }
}
