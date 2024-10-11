package com.example.demo;

import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.SplitPane;
import javafx.scene.input.KeyCode;
import javafx.scene.layout.Pane;
import javafx.scene.web.WebView;
import javafx.stage.Stage;
import org.junit.jupiter.api.Test;
import org.testfx.api.FxRobot;
import org.testfx.framework.junit5.ApplicationTest;
import org.testfx.matcher.control.LabeledMatchers;
import org.testfx.matcher.control.TextFlowMatchers;
import org.testfx.matcher.control.TextMatchers;

import static org.junit.jupiter.api.Assertions.*;
import static org.testfx.api.FxAssert.verifyThat;

class DashboardControllerTest extends ApplicationTest {

    @Override
    public void start(Stage stage) throws Exception {
        new Scenes(1300, 800, stage);
        stage.show();
    }

    @Test
    public void testInitializeNodeVisible() {
        clickOn("#submit");
        verifyThat("#topPane", Pane::isVisible);
        verifyThat("#mainPane", SplitPane::isVisible);
        verifyThat("#dr_ageWebView", Node::isVisible);
        verifyThat("#drAgePredicted", Node::isVisible);
        verifyThat("#drCalWebView", Node::isVisible);
        verifyThat("#lexisDiagramWebView", Node::isVisible);
        verifyThat("#APClexisDiagramWebView", Node::isVisible);
        verifyThat("#DefaultRateLabel", Node::isVisible);

        verifyThat("#DefaultRatePane", Node::isVisible);
        verifyThat("#LexisDiagramLabel", Node::isVisible);
        verifyThat("#APCLabel", Node::isVisible);
        //verifyThat("#LexisDiagramPane", Node::isVisible);
        verifyThat("#theme", Node::isVisible);
        verifyThat("#APCtheme", Node::isVisible);
        verifyThat("#uploadDataButton", Node::isVisible);

        verifyThat("#rootLayout", Node::isVisible);
        //verifyThat("#APCPane", Node::isVisible);
        verifyThat("#ageEffectWebView", Node::isVisible);
        verifyThat("#cohortEffectWebView", Node::isVisible);
        verifyThat("#periodEffectWebView", Node::isVisible);
        verifyThat("#APClexisDiagramWebView", Node::isVisible);
        verifyThat("#ErrorText", Node::isVisible);

        verifyThat("#adjustButton", Node::isVisible);
        verifyThat("#valueText", Node::isVisible);
        verifyThat("#featureText", Node::isVisible);
        verifyThat("#conditionValue", Node::isVisible);
        verifyThat("#goButton", Node::isVisible);
        //verifyThat("#infoPane", Node::isVisible);
        verifyThat("#separatorText", Node::isVisible);

        verifyThat("#ageText", Node::isVisible);
        verifyThat("#ageUnit", Node::isVisible);
        verifyThat("#cohortText", Node::isVisible);
        verifyThat("#cohortUnit", Node::isVisible);
        verifyThat("#defaultFlagText", Node::isVisible);
        verifyThat("#predictedDefaultRateText", Node::isVisible);
        verifyThat("#chooseFile", Node::isVisible);


    }

    @Test
    public void testUploadVisiable(){
        clickOn("#submit");
        clickOn("#uploadDataButton");
        verifyThat("#infoTitleLabel", Node::isVisible);
        verifyThat("#decimalLabel", Node::isVisible);
        verifyThat("#separatorLabel", Node::isVisible);
        verifyThat("#ageinfoLabel", Node::isVisible);
        verifyThat("#cohortinfoLabel", Node::isVisible);
        verifyThat("#defaultflaginfoLabel", Node::isVisible);
        verifyThat("#perdicteddefaultinfoLabel", Node::isVisible);
        verifyThat("#decimalText", Node::isVisible);
        verifyThat("#separatorText", Node::isVisible);
        verifyThat("#ageText", Node::isVisible);
        verifyThat("#cohortText", Node::isVisible);
        verifyThat("#defaultFlagText", Node::isVisible);
        verifyThat("#predictedDefaultRateText", Node::isVisible);
        verifyThat("#chooseFile", Node::isVisible);
    }

    @Test
    public void testNodeTextInTwoLanguages() {
        clickOn("#submit");
        clickOn("#language");
        FxRobot robot = new FxRobot();
        robot.press(KeyCode.DOWN);
        robot.release(KeyCode.DOWN);
        verifyThat("#title", LabeledMatchers.hasText("Credit Risk Visualisation"));
        verifyThat("#scaleText", LabeledMatchers.hasText("scale"));
        verifyThat("#DefaultRateLabel", LabeledMatchers.hasText("Default Rate"));
        robot.press(KeyCode.DOWN);
        robot.release(KeyCode.DOWN);
        verifyThat("#title", LabeledMatchers.hasText("信用风险可视化"));
        verifyThat("#scaleText", LabeledMatchers.hasText("比例"));
        verifyThat("#DefaultRateLabel", LabeledMatchers.hasText("违约率"));
    }
}