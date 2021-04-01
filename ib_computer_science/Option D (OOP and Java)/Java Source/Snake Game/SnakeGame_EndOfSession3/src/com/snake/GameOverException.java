package com.snake;

import com.snake.ui.ScoreBar;

/**
 * A Game Over Exception that stops the timer, and updates the status
 */
public class GameOverException extends Exception {

   private static final long serialVersionUID = 1L;

   public GameOverException(Board board, String message) {
      ScoreBar scoreBar = ScoreBar.getInstance();
      scoreBar.setStatus("Game Over: " + message + "    Press Enter to play again");

      if (board != null) {
         board.setTimer(false);
      }
   }
}
