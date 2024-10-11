package com.example.demo;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class Scenes {

    private final Stage stage;
    private final Scene loginScene;
    private Scene dashboardScene;
    private Scene settingsScene;
    private DashboardController dashboardController;
    private final LoginController loginController;
    private SettingsController settingsController;
    private int width = 1300;
    private int height = 1300;

    private String token;
    private boolean isDark = false;
    //possible value:
    // None;
    // redGreen for daltonism;
    // blueYellow for tetartanopia
    private String colorVision = "None";

    private String error = "0";

    private String feature = "null";
    private String condition = "null";
    private String value = "null";


    private String decimal = ".";
    private String separator = ",";
    private String age = "t";
    private String cohort = "v";
    private String defaultFlag = "y";
    private String predictedDefaultRate = "pd";
    private String ageUnit = "Month";
    private String cohortUnit = "Month";

    private String language = "English";
    private int fontSize = 14;


    /**
     * get Width value
     * @return value of widgh
     */
    public int getWidth(){return this.width;}

    /**
     * Get height value
     * @return height
     */
    public int getHeight(){return this.height;}
    /**
     * Get isDark value.
     * @return True if the user choose dark mode. False otherwise
     */
    public boolean getIsDark(){
        return this.isDark;
    }

    /**
     * Set the value of isDark
     * @param isDark The value of isDark.
     */
    public void setIsDark(boolean isDark){
        this.isDark = isDark;
    }

    /**
     * Get colorVision value.
     * @return colorVision value.
     */
    public String  getColorVision(){
        return this.colorVision;
    }

    /**
     * Set the value of colorVision
     * @param colorVision The value of colorVision.
     */
    public void setColorVision(String colorVision){
        this.colorVision = colorVision;
    }


    /**
     * Get token value.
     * @return String of token
     */
    public String getToken(){
        return this.token;
    }

    /**
     * Set value of token.
     * @param token The value of token.
     */
    public void setToken(String token) {
        this.token = token;
    }

    /**
     * Get error value.
     * @return String of error.
     */
    public String getError(){
        return this.error;
    }

    /**
     * Set value of error.
     * @param error The value of error.
     */
    public void setError(String error) {
        this.error = error;
    }

    /**
     * Get feature value.
     * @return String of feature.
     */
    public String getFeature(){
        return this.feature;
    }

    /**
     * Set value of feature.
     * @param feature The value of feature.
     */
    public void setFeature(String feature) {
        this.feature = feature;
    }

    /**
     * Get condition value.
     * @return String of condition.
     */
    public String getCondition(){
        return this.condition;
    }

    /**
     * Set value of condition.
     * @param condition The value of error.
     */
    public void setCondition(String condition) {
        switch (condition) {
            case ">" -> {
                this.condition = ">";
            }
            case "＜" -> {
                this.condition = "<";
            }
        }
    }

    /**
     * Get value value.
     * @return String of value.
     */
    public String getValue(){
        return this.value;
    }

    /**
     * Set value of value.
     * @param value The value of value.
     */
    public void setValue(String value) {
        this.value = value;
    }


    /**
     * Get decimal value.
     * @return String of decimal.
     */
    public String getDecimal(){
        return this.decimal;
    }

    /**
     * Set value of decimal.
     * @param decimal The value of decimal.
     */
    public void setDecimal(String decimal) {
        this.decimal = decimal;
    }

    /**
     * Get separator value.
     * @return String of separator.
     */
    public String getSeparator(){
        return this.separator;
    }

    /**
     * Set value of separator.
     * @param separator The value of separator.
     */
    public void setSeparator(String separator) {
        this.separator = separator;
    }


    /**
     * Get age value.
     * @return String of age.
     */
    public String getAge(){
        return this.age;
    }

    /**
     * Set value of age.
     * @param age The value of age.
     */
    public void setAge(String age) {
        this.age = age;
    }


    /**
     * Get cohort value.
     * @return String of cohort.
     */
    public String getCohort(){
        return this.cohort;
    }

    /**
     * Set value of cohort.
     * @param cohort The value of cohort.
     */
    public void setCohort(String cohort) {
        this.cohort = cohort;
    }


    /**
     * Get ageUnit value.
     * @return String of age unit.
     */
    public String getAgeUnit(){
        return this.ageUnit;
    }

    /**
     * Set value of ageUnit.
     * @param ageUnit The value of age unit.
     */
    public void setAgeUnit(String ageUnit) {
        this.ageUnit = ageUnit;
    }


    /**
     * Get cohort unit value.
     * @return String of cohort.
     */
    public String getCohortUnit(){
        return this.cohortUnit;
    }

    /**
     * Set value of cohort unit.
     * @param cohortUnit The value of cohort unit.
     */
    public void setCohortUnit(String cohortUnit) {
        this.cohortUnit = cohortUnit;
    }


    /**
     * Get defaultFlag value.
     * @return String of defaultFlag.
     */
    public String getDefaultFlag(){
        return this.defaultFlag;
    }

    /**
     * Set value of defaultFlag.
     * @param defaultFlag The value of defaultFlag.
     */
    public void setDefaultFlag(String defaultFlag) {
        this.defaultFlag = defaultFlag;
    }


    /**
     * Get predictedDefaultRate value.
     * @return String of predictedDefaultRate.
     */
    public String getPredictedDefaultRate(){
        return this.predictedDefaultRate;
    }

    /**
     * Set value of predictedDefaultRate.
     * @param predictedDefaultRate The value of predictedDefaultRate.
     */
    public void setPredictedDefaultRate(String predictedDefaultRate) {
        this.predictedDefaultRate = predictedDefaultRate;
    }

    /**
     * Get language value.
     * @return String of language.
     */
    public String getLanguage(){
        return this.language;
    }

    /**
     * Set value of language.
     * @param language The value of language.
     */
    public void setLanguage(String language) {
        this.language = language;
    }

    /**
     * Get fontsize value.
     * @return String of language.
     */
    public int getFontSize(){
        return this.fontSize;
    }

    /**
     * Set value of fontSize.
     * @param fontSize The value of language.
     */
    public void setFontSize(int fontSize) {
        this.fontSize = fontSize;
        Parent setiingRoot = settingsScene.getRoot();
        setiingRoot.setStyle("-fx-font-size: " + fontSize
                + ";-fx-font: Times New Roman;-fx-alignment: center;");
        Parent dashboardRoot = dashboardScene.getRoot();
        dashboardRoot.setStyle("-fx-font-size: " + fontSize
                + ";-fx-font: Times New Roman;-fx-alignment: center;");
        Parent loginRoot = loginScene.getRoot();
        loginRoot.setStyle("-fx-font-size: " + fontSize +
                ";-fx-font: Times New Roman;-fx-alignment: center;");
    }


    /**
     * constructor of Scenes.
     * @param width Width of the windows.
     * @param height Height of the windows.
     * @param stage Stage of the windows.
     * @throws IOException Class instance storing FXML and their controllers
     *                     provide interface for controllers to interact
     *                     with each other.
     */
    public Scenes(int width, int height, Stage stage) throws IOException {
        this.stage = stage;
        this.width = width;
        this.height = height;
        FXMLLoader loginLoader = new FXMLLoader(HelloApplication.class.
                getResource("login.fxml"));

        this.loginScene = new Scene(loginLoader.load(), width, height);

        this.loginController = loginLoader.getController();

        this.loginController.initData(this);

        stage.setScene(this.loginScene);
    }


    /**
     * Initialize dashboard page.
     * @throws IOException Class instance storing FXML and their controllers
     *                     provide interface for controllers to interact
     *                     with each other.
     */
    public void initializeDashboard() throws IOException {
        FXMLLoader dashboardLoader = new FXMLLoader(
                HelloApplication.class.getResource("dashboard.fxml"));
        this.dashboardScene = new Scene(
                dashboardLoader.load(), this.width, this.height);
        this.dashboardController = dashboardLoader.getController();
        this.dashboardController.initData(this);
        Parent dashboardRoot = dashboardScene.getRoot();
        dashboardRoot.setStyle("-fx-font-size: " + fontSize
                + ";-fx-font: Times New Roman;-fx-alignment: center;");
    }


    /**
     * Initialize settings page.
     * @throws IOException Class instance storing FXML and their controllers
     *                     provide interface for controllers to interact
     *                     with each other.
     */
    public void initializeSettings() throws IOException {
        FXMLLoader settingsLoader = new FXMLLoader(
                HelloApplication.class.getResource("settings.fxml"));
        this.settingsScene = new Scene(
                settingsLoader.load(), this.width, this.height);
        this.settingsController = settingsLoader.getController();
        this.settingsController.initData(this);
        Parent settingsRoot = settingsScene.getRoot();
        settingsRoot.setStyle("-fx-font-size: " + fontSize
                + ";-fx-font: Times New Roman;-fx-alignment: center;");
    }


    /**
     * Get loginScene.
     * @return Scene of loginScene.
     */
    public Scene getLoginScene() {
        return loginScene;
    }

    /**
     * Get dashboardScene.
     * @return Scene of dashboardScene.
     */
    public Scene getDashboardScene() {
        return dashboardScene;
    }

    /**
     * Get stage
     * @return Stage of scene.
     */
    public Stage getStage() {
        return stage;
    }


    /**
     * Get SettingsScene.
     * @return Scene of SettingsScene.
     */
    public Scene getSettingsScene() { return settingsScene;}


    /**
     * Get dashboardController
     * @return controller of dashboard.
     */
    public DashboardController getDashboardController(){
        return dashboardController;}

    public void openDarkMode(){
        try {
            loginScene.getStylesheets().add("dark-theme.css");
            dashboardScene.getStylesheets().add("dark-theme.css");
            settingsScene.getStylesheets().add("dark-theme.css");
        }catch(Exception e){};
    }

    public void closeDarkMode(){
        try{loginScene.getStylesheets().remove("dark-theme.css");
            dashboardScene.getStylesheets().remove("dark-theme.css");
            settingsScene.getStylesheets().remove("dark-theme.css");
        }catch(Exception e){};
    }
}
