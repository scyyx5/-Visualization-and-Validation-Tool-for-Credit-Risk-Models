package com.example.demo;

import javafx.animation.RotateTransition;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.*;
import com.example.demo.API.UserAPI;
import javafx.scene.text.Text;
import javafx.util.Duration;

import java.io.FileWriter;   // Import the FileWriter class
import java.io.IOException;
import java.net.MalformedURLException;

public class LoginController {

    @FXML
    private Text titleLabel;
    @FXML
    private TextField email;
    @FXML
    private Text emailLabel;

    @FXML
    private TextField password;

    @FXML
    private Text passwordLabel;

    @FXML
    private Button submit;

    @FXML
    private AnchorPane pane;

    private Scenes scenes;
    @FXML
    private Pane loadingPane;

    @FXML
    private ImageView loadingImage;
    @FXML
    private ComboBox<String> language;


    /**
     * Store class instance of Scenes to manage data
     * @param scenes Class instance storing FXML and their controllers
     *             provide interface for controllers to interact with each other
     */
    public void initData(Scenes scenes) {
        this.scenes = scenes;
        loadingPane.setVisible(false);
        Image image = new Image("file:res/dashboard_background.jpg");
        BackgroundImage bgImage = new BackgroundImage(image,
                BackgroundRepeat.NO_REPEAT, BackgroundRepeat.NO_REPEAT,
                BackgroundPosition.CENTER, BackgroundSize.DEFAULT);
        pane.setBackground(new Background(bgImage));

    }

    /**
     * Write token into the files
     * @param filename The file to store tokens for the users
     * @param token The string of token
     */
    private void writeToken(String filename, String token) {
        try {
            FileWriter myWriter = new FileWriter(filename);
            myWriter.write(token);
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    /**
     * The event after clicking login button: send log in request,
     * get users' token, and load dashboard.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *             and bubbling phases described at EventDispatcher
     * @throws IOException Signals that an I/O exception to some sort has
     *                     occurred.This class is the general class of exception
     *                     produced by failed or interrupted I/O operations.
     */
    @FXML
    void loginClicked(MouseEvent event) throws IOException, InterruptedException {
        long stime = System.nanoTime();
        loadingPane.setVisible(true);
        Duration duration = Duration.millis(2000);
        //Create new rotate transition
        RotateTransition rotateTransition = new RotateTransition(
                duration, loadingImage);
        //Rotate by 360 degree
        rotateTransition.setByAngle(360);
        rotateTransition.play();

        UserAPI user = new UserAPI();
        String token = user.login("http://127.0.0.1:8000/api/v4/login/",
                email.getText(),password.getText());
        //String token = user.login("http://127.0.0.1:8000/api/v4/login/",
        //        "test@gmail.com","test123456");
        scenes.setToken(token);
        scenes.initializeDashboard();

        writeToken("token.txt", token);
        try {
            scenes.getDashboardController().updateGraph(
                    scenes.getIsDark(),"simDTS",token);
            scenes.getDashboardController().loadGraph();
        } catch (MalformedURLException ex) {
            throw new RuntimeException(ex);
        }
        rotateTransition.setOnFinished(e -> {
            try {
                scenes.getDashboardController().updateTheme(scenes.getIsDark());
            } catch (MalformedURLException ex) {
                throw new RuntimeException(ex);
            }

            this.scenes.getStage().setScene(this.scenes.getDashboardScene());
        });
        long etime = System.nanoTime();
        System.out.printf("login time: %d", (etime - stime));
    }

    /**
     * Change unit of cohort.
     * @throws MalformedURLException Thrown to indicate that a malformed
     *              URL has occurred.Either no legal protocol could be found in
     *              a specification string or the string could not be parsed.
     */
    @FXML
    private void changeLanguage() throws MalformedURLException {
        long stime = System.nanoTime();
        String s = language.getSelectionModel().getSelectedItem();
        switch (s){
            case "English" -> {
                this.titleLabel.setText("Credit Risk Visualization");
                this.emailLabel.setText("✉ Email");
                this.passwordLabel.setText("🔑 Password");
                this.submit.setText("🔓 Login");
                this.scenes.setLanguage("English");
            }
            case "简体中文" -> {
                this.titleLabel.setText("信用风险可视化");
                this.emailLabel.setText("✉ 邮箱");
                this.passwordLabel.setText("🔑 密码");
                this.submit.setText("🔓 登录");
                this.scenes.setLanguage("Chinese");
            }
        }
        long etime = System.nanoTime();
        System.out.printf("change language time: %d", (etime - stime));
    }
}
