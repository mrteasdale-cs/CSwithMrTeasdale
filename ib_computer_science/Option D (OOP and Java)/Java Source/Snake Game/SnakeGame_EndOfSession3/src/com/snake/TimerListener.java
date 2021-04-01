package com.snake;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.Timer;

public class TimerListener implements ActionListener {

   private Snake snake;
   boolean gameOver = false;

   public TimerListener(Snake snake) {
      this.snake = snake;
   }

   private void moveSnake() throws Exception {
      // Put your code here to move the Snake!
      // Remember that you can do this calling your snake.move() method
      try {
         snake.updateDirections();
         snake.move();
      } catch (ArrayIndexOutOfBoundsException ex) {
         throw new GameOverException(null, "Snake out of bounds");
      }

   }

   @Override
   public void actionPerformed(ActionEvent e) {

      if (!(e.getSource() instanceof Timer)) {
         return;
      }

      snake.resetDirectionChangedThisTurn();

      if (gameOver == true) {
         return;
      }

      try {
         moveSnake();
      } catch (GameOverException ex) {
         gameOver = true;
      } catch (Exception e1) {
         e1.printStackTrace();
      }
   }
}
