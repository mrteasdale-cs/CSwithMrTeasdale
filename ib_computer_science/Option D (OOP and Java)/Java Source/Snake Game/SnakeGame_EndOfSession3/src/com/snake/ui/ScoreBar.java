package com.snake.ui;

import java.awt.BorderLayout;
import javax.swing.JLabel;
import javax.swing.JPanel;

/**
 * This class represents the ScoreBar at the bottom of the UI.
 */
public class ScoreBar extends JPanel {
	
	private static final long serialVersionUID = 1L;

    // Note these variables are private - they can only be
    // accessed in this class. You will need to write public methods
    // to access these from any other class. 'setScoreLabel' has been given
    // as an example
    private JLabel scoreLabel = new JLabel("Score: 0");
	private JLabel statusLabel = new JLabel("Press Enter to start");

    private static ScoreBar instance = null;

    /**
     * Constructor for the ScoreBar class, this adds the labels for
     * the score and status. Note this is private! A ScoreBar object
     * can only be accessed by calling ScoreBar.getInstance();
     */
    private ScoreBar() {
		add(scoreLabel, BorderLayout.WEST);
		add(new JLabel("             "), BorderLayout.CENTER);
		add(statusLabel, BorderLayout.EAST);
	}

    /**
     * This is the only way to get the instance of the ScoreBar object.
     * This method should be used instead of passing around a scorebar object.
     */
    public static synchronized ScoreBar getInstance() {
       if (instance == null) {
          instance = new ScoreBar();
       }
       return instance;
    }

    /**
     * Set the score label, used when a piece of food has been eaten.
     * @param score - int: the current score
     */
    public void setScoreLabel(int score) {
       scoreLabel.setText("Score: " + score);
    }

    public void setStatus(String status) {
       statusLabel.setText(status);
    }
}
