package com.example.demo;

import javafx.event.Event;
import javafx.fxml.FXML;
import javafx.event.ActionEvent;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Slider;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;

import java.io.IOException;
import java.net.MalformedURLException;



public class SettingsController {

    @FXML
    private Scenes scenes;

    @FXML
    private Pane rootLayout;

    @FXML
    private Button backButton;

    @FXML
    private CheckBox DarkCheck;

    @FXML
    private ComboBox<String> colorVision;
    @FXML
    private Slider fontSlider;

    private int fontSize;



    /**
     * Store class instance of Scenes to manage data
     * @param scenes Class instance storing FXML and their controllers
     *             provide interface for controllers to interact with each other
     */
    @FXML
    public void initData(Scenes scenes) {
        this.scenes = scenes;
    }


    /**
     * The event after clicking back button.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *             and bubbling phases described at EventDispatcher
     * @throws IOException Signals that an I/O exception to some sort has
     *                   occurred. This class is the general class of exceptions
     *                   produced by failed or interrupted I/O operations.
     */
    @FXML
    void backClicked(ActionEvent event) throws IOException {
        //scenes.initializeDashboard();
        this.fontSize = (int) fontSlider.getValue();
        scenes.setFontSize(this.fontSize);
        scenes.getDashboardController().updateGraph(scenes.getIsDark(),
                "sim",scenes.getToken());
        this.scenes.getStage().setScene(this.scenes.getDashboardScene());
    }


    /**
     * The event after clicking color vision check.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     * @throws MalformedURLException Thrown to indicate that a malformed URL has
     *              occurred. Either no legal protocol could be found in a
     *              specification string or the string could not be parsed.
     */
    @FXML
    void onDarkCheckClick(ActionEvent event) throws MalformedURLException {
        if(DarkCheck.isSelected()){
            scenes.setIsDark(true);
            scenes.openDarkMode();
        }else{
            scenes.setIsDark(false);
            scenes.closeDarkMode();
        }
    }

    /**
     * Change color vision.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     * @throws MalformedURLException Thrown to indicate that a malformed URL has
     *              occurred. Either no legal protocol could be found in a
     *              specification string or the string could not be parsed.
     */
    @FXML
    void changeColorVision(ActionEvent event) throws MalformedURLException {
        String s = colorVision.getSelectionModel().getSelectedItem();
        switch (s){
            case "None" -> {
                scenes.setColorVision("None");
            }
            case "daltonism" -> {
                scenes.setColorVision("redGreen");
            }
            case "tetartanopia" -> {
                scenes.setColorVision("blueYellow");
            }
            case "monochromasia" ->{
                scenes.setColorVision("full");
            }
        }
    }





}
