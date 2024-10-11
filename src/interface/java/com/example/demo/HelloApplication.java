package com.example.demo;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;


public class HelloApplication extends Application {

    private static Scene scene;
    @Override
    public void start(Stage stage) throws IOException {

        new Scenes(1300, 800, stage);
        stage.setTitle("credit risk visualization");
        stage.show();

    }

    public static void main(String[] args) {
        launch();
    }
}

