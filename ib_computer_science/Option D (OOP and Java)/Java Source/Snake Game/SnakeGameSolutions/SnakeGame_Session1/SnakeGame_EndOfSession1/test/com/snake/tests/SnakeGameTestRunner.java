/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.snake.tests;

import junit.textui.TestRunner;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.runner.JUnitCore;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

/**
 *
 * @author Sean
 */
@RunWith(Suite.class)
@Suite.SuiteClasses({snakegametest.tests.ui.SnakeUITest.class, snakegametest.tests.BoardTest.class,
							snakegametest.tests.CellTest.class, snakegametest.tests.ui.BoardUITest.class,
							snakegametest.tests.SnakeTest.class})
public class SnakeGameTestRunner {


}
