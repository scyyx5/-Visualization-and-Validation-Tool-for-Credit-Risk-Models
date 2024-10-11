package com.example.demo;

import com.example.demo.Scenes;
import javafx.scene.Node;
import javafx.scene.control.ComboBox;
import javafx.scene.input.KeyCode;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;
import org.junit.jupiter.api.Test;
import org.testfx.api.FxRobot;
import org.testfx.framework.junit5.ApplicationTest;
import org.testfx.matcher.control.TextMatchers;

import java.io.IOException;

import static org.junit.jupiter.api.Test.*;
import static org.testfx.api.FxAssert.verifyThat;
import static org.testfx.matcher.control.LabeledMatchers.hasText;

class LoginControllerTest extends ApplicationTest {

    @Override
    public void start(Stage stage) throws Exception {
        new Scenes(1300, 800, stage);
        stage.show();
    }

    @Test
    public void testNodeVisible() {
        verifyThat("#pane", AnchorPane::isVisible);
        verifyThat("#titleLabel", Node::isVisible);
        verifyThat("#emailLabel", Node::isVisible);
        verifyThat("#passwordLabel", Node::isVisible);
        verifyThat("#email", Node::isVisible);
        verifyThat("#password", Node::isVisible);
        verifyThat("#submit", Node::isVisible);
        verifyThat("#pane", Node::isVisible);
    }

    @Test
    public void testNodeTextInTwoLanguages() {
        clickOn("#language");
        FxRobot robot = new FxRobot();
        robot.press(KeyCode.DOWN);
        robot.release(KeyCode.DOWN);
        verifyThat("#titleLabel", TextMatchers.hasText("Credit Risk Visualization"));
        verifyThat("#emailLabel", TextMatchers.hasText("✉ Email"));
        verifyThat("#passwordLabel", TextMatchers.hasText("🔑 Password"));
        robot.press(KeyCode.DOWN);
        robot.release(KeyCode.DOWN);
        verifyThat("#titleLabel", TextMatchers.hasText("信用风险可视化"));
        verifyThat("#emailLabel", TextMatchers.hasText("✉ 邮箱"));
        verifyThat("#passwordLabel", TextMatchers.hasText("🔑 密码"));
    }
}