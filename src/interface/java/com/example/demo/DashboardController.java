package com.example.demo;
import com.example.demo.API.AdjustAPI;
import com.example.demo.API.LoadGraphAPI;
import javafx.animation.RotateTransition;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.*;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import javafx.util.Duration;
import java.io.*;
import java.net.MalformedURLException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;


public class DashboardController {

    //String of URL.
    public final String URL = "http://127.0.0.1:8000/";
    @FXML
    private Stage stage;
    @FXML
    private WebView drAgeWebView;
    WebEngine drAgewebEngine = null;
    @FXML
    private CheckBox drAgePredicted;
    @FXML
    private WebView drCalWebView;
    WebEngine drCalwebEngine = null;
    @FXML
    private CheckBox drCalPredicted;
    @FXML
    private WebView lexisDiagramWebView;
    WebEngine lexisDiagramEngine = null;
    WebEngine apcLexisDiagramEngine = null;
    WebEngine realAPCLexisDiagramEngine = null;
    @FXML
    private WebView APClexisDiagramWebView;
    @FXML
    private WebView realAPClexisDiagramWebView;

    @FXML
    private Button DefaultRateLabel;
    @FXML
    private Pane DefaultRatePane;
    @FXML
    private Button LexisDiagramLabel;

    @FXML
    private Button SettengsButton;

    @FXML
    private Button APCLabel;
    @FXML
    private Pane LexisDiagramPane;
    @FXML
    private ComboBox<String> theme;
    @FXML
    private ComboBox<String> APCtheme;
    @FXML
    private ComboBox<String> realAPCtheme;
    @FXML
    private Button uploadDataButton;

    @FXML
    private VBox rootLayout;

    @FXML
    private Pane APCPane;
    @FXML
    private WebView ageEffectWebView;

    @FXML
    private WebView cohortEffectWebView;

    @FXML
    private Label title;

    @FXML
    private Label scaleText;

    @FXML
    private Label error;


    @FXML
    private Label featureLabel;

    @FXML
    private Label conditionLabel;

    @FXML
    private Label valueLabel;
    @FXML
    private WebView periodEffectWebView;
    WebEngine ageEngine = null;
    WebEngine cohortEngine = null;
    WebEngine periodEngine = null;
    //String of tokens
    private String token;
    @FXML
    private TextField ErrorText;
    @FXML
    private Button adjustButton;
    @FXML
    private TextField valueText;
    @FXML
    private TextField featureText;
    @FXML
    private ComboBox<String> conditionValue;

    private Scenes scenes;
    @FXML
    private Button goButton;
    @FXML
    private Pane infoPane;
    @FXML
    private TextField decimalText;
    @FXML
    private TextField separatorText;
    @FXML
    private TextField ageText;
    @FXML
    private ComboBox<String> ageUnit;
    @FXML
    private TextField cohortText;
    @FXML
    private ComboBox<String> cohortUnit;
    @FXML
    private TextField defaultFlagText;
    @FXML
    private TextField predictedDefaultRateText;
    @FXML
    private Button chooseFile;
    @FXML
    private Pane loadingPane;
    @FXML
    private ImageView loadingImage;
    @FXML
    private Tab ageeffectID;

    @FXML
    private Tab periodeffectID;
    @FXML
    private Tab cohorteffectID;
    @FXML
    private Tab ageID;
    @FXML
    private Tab calID;
    @FXML
    private Tab preAPCID;
    @FXML
    private Tab realAPCID;
    @FXML
    private Tab realID;

    private String feature = "None";
    private String condition = "None";
    private String value = "None";

    @FXML
    private ComboBox<String> scale;
    private String scalePrefix = "";

    @FXML
    private ComboBox<String> language;



    /**
     * Store class instance of Scenes to manage data
     * @param scenes Class instance storing FXML and their controllers provide
     *               interface for controllers to interact with each other
     */
    public void initData(Scenes scenes) throws MalformedURLException {
        this.scenes = scenes;
        Image image = new Image("file:res/dashboard_background.jpg");
        BackgroundImage bgImage = new BackgroundImage(image,
                BackgroundRepeat.NO_REPEAT, BackgroundRepeat.NO_REPEAT,
                BackgroundPosition.CENTER, BackgroundSize.DEFAULT);
        rootLayout.setBackground(new Background(bgImage));
        if (scenes.getLanguage() != "English") {
            this.language.setPromptText("简体中文");
            this.setChinese();
        }
    }



    /**
     *
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *             and bubbling phases described at EventDispatcher
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *        has occurred. Either no legal protocol could be found
     *       in a specification string or the string could not be parsed.
     */
    @FXML
    void ondrAgePredictedButtonClick(ActionEvent event) throws MalformedURLException {
        if (drAgePredicted.isSelected()) {
            File f = new File("res\\" +
                    scalePrefix + "dr_age_predicted.html");
            drAgewebEngine.load(f.toURI().toURL().toString());
        } else {
            File f = new File("res\\" +
                    scalePrefix + "dr_age.html");
            drAgewebEngine.load(f.toURI().toURL().toString());
        }

    }



    /**
     * The event after clicking upload data button.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *             and bubbling phases described at EventDispatcher
     * @throws IOException Signals that an I/O exception to some sort has 
     *                    occurred. This class is the general class of exception
     *                    produced by failed or interrupted I/O operations.
     */
    @FXML
    void uploadDataClicked(MouseEvent event) throws IOException {
        infoPane.setVisible(true);
    }



    /**
     * The event after clicking choose file button.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *             and bubbling phases described at EventDispatcher
     * @throws IOException Signals that an I/O exception to some sort has 
     *                    occurred. This class is the general class of exception
     *                    produced by failed or interrupted I/O operations.
     */
    @FXML
    void chooseFileClicked(MouseEvent event) throws IOException {
        long stime = System.nanoTime();
        loadingPane.setVisible(true);
        scenes.setDecimal(decimalText.getText());
        scenes.setSeparator(separatorText.getText());
        scenes.setAge(ageText.getText());
        scenes.setCohort(cohortText.getText());
        scenes.setDefaultFlag(defaultFlagText.getText());
        scenes.setPredictedDefaultRate(predictedDefaultRateText.getText());
        infoPane.setVisible(false);

        scenes.setError("0");
        scenes.setFeature("null");
        scenes.setCondition("null");
        scenes.setValue("null");

        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Open Resource File");
        this.stage = this.scenes.getStage();
        File file = fileChooser.showOpenDialog(stage);
        fileChooser.setTitle("Choose dataset");
        fileChooser.setInitialDirectory(
                new File(System.getProperty("user.home")));
        fileChooser.getExtensionFilters().addAll(
                //new FileChooser.ExtensionFilter("All Images", "*.*"),
                new FileChooser.ExtensionFilter("CSV", "*.csv")
                //new FileChooser.ExtensionFilter("GIF", "*.gif"),
                //new FileChooser.ExtensionFilter("BMP", "*.bmp"),
                //new FileChooser.ExtensionFilter("PNG", "*.png")
        );
        try {
            Path path = Paths.get("src\\visualization\\sim.csv");
            Files.delete(path);
        } finally {

        }
        Files.copy(file.toPath(), Path.of("src\\visualization\\sim.csv"));
        Duration duration = Duration.millis(2000);
        //Create new rotate transition
        RotateTransition rotateTransition = new RotateTransition(
                duration, loadingImage);

        //Rotate by 360 degree
        rotateTransition.setByAngle(360);
        rotateTransition.play();
        initializeParameter();
        LoadGraphAPI.load("http://127.0.0.1:8000/api/v4/download_graph/",
                token, "sim", scenes.getIsDark(),
                scenes.getColorVision(),scenes.getError(),
                this.feature,this.condition,this.value,
                scenes.getDecimal(),scenes.getSeparator(),
                scenes.getAge(),scenes.getAgeUnit(),scenes.getCohort(),
                scenes.getCohortUnit(),scenes.getDefaultFlag(),
                scenes.getPredictedDefaultRate(),scenes.getLanguage());
        rotateTransition.setOnFinished(e -> {
            try {
                loadGraph();
            } catch (MalformedURLException ex) {
                throw new RuntimeException(ex);
            }
            loadingPane.setVisible(false);
        });
        long etime = System.nanoTime();
        System.out.printf("upload time: %d", (etime - stime));


    }


    /**
     * Initialize all the parameters for error and filtering.
     */
    void initializeParameter(){
        scenes.setError("0");
        scenes.setFeature("null");
        scenes.setCondition("null");
        scenes.setValue("null");
    }

    /**
     * The event after clicking settings button.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *             and bubbling phases described at EventDispatcher
     * @throws IOException Signals that an I/O exception to some sort has 
     *                    occurred. This class is the general class of exception
     *                    produced by failed or interrupted I/O operations.
     */
    @FXML
    void settingsClicked(MouseEvent event) throws IOException{
        if(scenes.getSettingsScene() == null){
            scenes.initializeSettings();
        }
        this.scenes.getStage().setScene(this.scenes.getSettingsScene());
    }


    /**
     * The event after clicking go button.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    void goButtonClicked(MouseEvent event) throws MalformedURLException {
        long stime = System.nanoTime();
        scenes.setFeature(featureText.getText());
        scenes.setValue(valueText.getText());
        scenes.setCondition(conditionValue.getSelectionModel().getSelectedItem());
        loadingPane.setVisible(true);
        Duration duration = Duration.millis(2000);
        //Create new rotate transition
        RotateTransition rotateTransition = new RotateTransition(
                duration, loadingImage);
        //Rotate by 360 degree
        rotateTransition.setByAngle(360);
        rotateTransition.play();
        LoadGraphAPI.load("http://127.0.0.1:8000/api/v4/download_graph/",
                token, "sim", scenes.getIsDark(),scenes.getColorVision(),
                scenes.getError(), scenes.getFeature(),scenes.getCondition(),
                scenes.getValue(), scenes.getDecimal(),scenes.getSeparator(),
                scenes.getAge(), scenes.getAgeUnit(),scenes.getCohort(),
                scenes.getCohortUnit(),scenes.getDefaultFlag(),
                scenes.getPredictedDefaultRate(), scenes.getLanguage());
        rotateTransition.setOnFinished(e -> {
            try {
                loadGraph();
            } catch (MalformedURLException ex) {
                throw new RuntimeException(ex);
            }
            loadingPane.setVisible(false);
        });
        long etime = System.nanoTime();
        System.out.printf("filter: %d", (etime - stime));
    }


    /**
     * The event after clicking adjust button.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    void adjustButtonClicked(MouseEvent event) throws MalformedURLException {
        long stime = System.nanoTime();
        scenes.setError(ErrorText.getText());
        AdjustAPI adjust = new AdjustAPI();
        loadingPane.setVisible(true);
        Duration duration = Duration.millis(2000);
        //Create new rotate transition
        RotateTransition rotateTransition = new RotateTransition(
                duration, loadingImage);
        //Rotate by 360 degree
        rotateTransition.setByAngle(360);
        rotateTransition.play();
        rotateTransition.setOnFinished(e -> {
            adjust.adjustAPC("http://127.0.0.1:8000/api/v4/adjust/",
                    token, "sim",
                    scenes.getIsDark(), scenes.getError(),
                    scenes.getFeature(),scenes.getCondition(),scenes.getValue(),
                    scenes.getAgeUnit(),scenes.getCohortUnit(),
                    scenes.getDecimal(),scenes.getSeparator());
            try {
                loadAPCGraph();
            } catch (MalformedURLException ex) {
                throw new RuntimeException(ex);
            }
            loadingPane.setVisible(false);
        });
        long etime = System.nanoTime();
        System.out.printf("adjustment time: %d", (etime - stime));
    }

    /**
     * The event after clicking predicted button.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    void ondrCalPredictedButtonClick(ActionEvent event) throws MalformedURLException {
        if(drCalPredicted.isSelected()){
            File f = new File("res\\" +
                    scalePrefix + "dr_cal_predicted.html");
            drCalwebEngine.load(f.toURI().toURL().toString());
        }else{
            File f = new File("res\\" +
                    scalePrefix + "dr_cal.html");
            drCalwebEngine.load(f.toURI().toURL().toString());
        }
    }





    /**
     * Click default rate button.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     */
    public void clickDefaultRate(ActionEvent event) {
        DefaultRatePane.setVisible(true);
        LexisDiagramPane.setVisible(false);
        APCPane.setVisible(false);
    }


    /**
     * click lexis diagram button.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     */
    public void clickLexisDiagram(ActionEvent event) {
        DefaultRatePane.setVisible(false);
        LexisDiagramPane.setVisible(true);
        APCPane.setVisible(false);
    }



    /**
     * click APC button.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     */
    public void clickAPC(ActionEvent event) {
        DefaultRatePane.setVisible(false);
        LexisDiagramPane.setVisible(false);
        APCPane.setVisible(true);
    }



    /**
     * Change condition.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    void changeCondition(ActionEvent event) throws MalformedURLException {
        String s = conditionValue.getSelectionModel().getSelectedItem();
        switch (s){
            case ">" -> {
                this.condition = ">";
            }
            case "＜" -> {
                this.condition = "<";
            }
        }
    }



    /**
     * Change APC theme.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    void changeAPCTheme(ActionEvent event) throws MalformedURLException {
        String s = APCtheme.getSelectionModel().getSelectedItem();
        switch (s){
            case "hot" -> {
                File apcLexisDiagram = new File("res\\"
                        +  scalePrefix + "apc_lexis_diagram_hot_r.html");
                apcLexisDiagramEngine.load(
                    apcLexisDiagram.toURI().toURL().toString());
            }
            case "Green_Blue" -> {
                File apcLexisDiagram = new File("res\\" 
                        + scalePrefix + "apc_lexis_diagram_YlGnBu.html");
                apcLexisDiagramEngine.load(
                    apcLexisDiagram.toURI().toURL().toString());
            }
            case "Oranges" -> {
                File apcLexisDiagram = new File("res\\" 
                        + scalePrefix + "apc_lexis_diagram_OrRd.html");
                apcLexisDiagramEngine.load(
                    apcLexisDiagram.toURI().toURL().toString());
            }
            case "grey" -> {
                File apcLexisDiagram = new File("res\\" 
                        + scalePrefix + "apc_lexis_diagram_greys.html");
                apcLexisDiagramEngine.load(
                    apcLexisDiagram.toURI().toURL().toString());
            }
            default -> {
                File apcLexisDiagram = new File("res\\" 
                        + scalePrefix + "apc_lexis_diagram_" + s + ".html");
                apcLexisDiagramEngine.load(
                    apcLexisDiagram.toURI().toURL().toString());
            }
        }
    }

    /**
     * Change APC theme.
     * @param event When mouse event occurs, the top-most node under cursor
     *              is picked and the event is delivered to it through capturing
     *              and bubbling phases described at EventDispatcher
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    void changerealAPCTheme(ActionEvent event) throws MalformedURLException {
        String s = realAPCtheme.getSelectionModel().getSelectedItem();
        switch (s){
            case "hot" -> {
                File apcLexisDiagram = new File("res\\" 
                    + scalePrefix + "real_apc_lexis_diagram_hot_r.html");
                realAPCLexisDiagramEngine.load(
                        apcLexisDiagram.toURI().toURL().toString());
            }
            case "Green_Blue" -> {
                File apcLexisDiagram = new File("res\\" 
                    + scalePrefix + "real_apc_lexis_diagram_YlGnBu.html");
                realAPCLexisDiagramEngine.load(
                        apcLexisDiagram.toURI().toURL().toString());
            }
            case "Oranges" -> {
                File apcLexisDiagram = new File("res\\" 
                    + scalePrefix + "real_apc_lexis_diagram_OrRd.html");
                realAPCLexisDiagramEngine.load(
                        apcLexisDiagram.toURI().toURL().toString());
            }
            case "grey" -> {
                File apcLexisDiagram = new File("res\\" 
                    + scalePrefix + "real_apc_lexis_diagram_greys.html");
                realAPCLexisDiagramEngine.load(
                        apcLexisDiagram.toURI().toURL().toString());
            }
            default -> {
                File apcLexisDiagram = new File("res\\" 
                    + scalePrefix + "real_apc_lexis_diagram_" + s + ".html");
                realAPCLexisDiagramEngine.load(
                        apcLexisDiagram.toURI().toURL().toString());
            }
        }
    }

    /**
     * Change theme.
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    private void changeTheme() throws MalformedURLException {
        String s = theme.getSelectionModel().getSelectedItem();
        switch (s){
            case "hot" -> {
                File lexisDiagram = new File("res\\" 
                       + scalePrefix + "lexis_diagram_hot_r.html");
                lexisDiagramEngine.load(lexisDiagram.toURI().toURL().toString());
            }
            case "Green_Blue" -> {
                File lexisDiagram = new File("res\\" 
                       + scalePrefix + "lexis_diagram_YlGnBu.html");
                lexisDiagramEngine.load(lexisDiagram.toURI().toURL().toString());
            }
            case "Oranges" -> {
                File lexisDiagram = new File("res\\" 
                       + scalePrefix + "lexis_diagram_OrRd.html");
                lexisDiagramEngine.load(lexisDiagram.toURI().toURL().toString());
            }
            case "grey" -> {
                File lexisDiagram = new File("res\\" 
                       + scalePrefix + "lexis_diagram_greys.html");
                lexisDiagramEngine.load(lexisDiagram.toURI().toURL().toString());
            }
            default -> {
                File lexisDiagram = new File("res\\" 
                       + scalePrefix + "lexis_diagram_" + s + ".html");
                lexisDiagramEngine.load(lexisDiagram.toURI().toURL().toString());
            }
        }
    }



    /**
     * Change drage scale.
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    void changeScale() throws MalformedURLException {
        long stime = System.nanoTime();
        String s = scale.getSelectionModel().getSelectedItem();
        switch (s){
            case "1" -> {
                scalePrefix = "";
            }
            case "sinh" -> {
                scalePrefix = "sinh_";
            }
            case "exp" -> {
                scalePrefix = "exp_";
            }
        }
        loadGraph();
        long etime = System.nanoTime();
        System.out.printf("change scale time: %d", (etime - stime));
    }


    /**
     * Change unit of age.
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    private void changeAgeUnit() throws MalformedURLException {
        String s = ageUnit.getSelectionModel().getSelectedItem();
        switch (s){
            case "Month" -> {
                scenes.setAgeUnit("Month");
            }
            case "Day" -> {
                scenes.setAgeUnit("Day");
            }
            case "Year" -> {
                scenes.setAgeUnit("Year");
            }
        }
    }


    /**
     * Change unit of cohort.
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    private void changeCohortUnit() throws MalformedURLException {
        String s = cohortUnit.getSelectionModel().getSelectedItem();
        switch (s){
            case "Month" -> {
                scenes.setCohortUnit("Month");
            }
            case "Day" -> {
                scenes.setCohortUnit("Day");
            }
            case "Year" -> {
                scenes.setCohortUnit("Year");
            }
        }
    }

    /**
     * Change unit of cohort.
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    @FXML
    private void changeLanguage() throws MalformedURLException {
        String s = language.getSelectionModel().getSelectedItem();
        switch (s){
            case "English" -> {
                this.setEnglish();
                this.scenes.setLanguage("English");
            }
            case "简体中文" -> {
                this.setChinese();
                this.scenes.setLanguage("Chinese");

            }
        }
        updateGraph(scenes.getIsDark(),"sim",scenes.getToken());

    }


    /**
     * Set language as English
     */
    private void setEnglish() {
        this.title.setText("Credit Risk Visualisation");
        this.uploadDataButton.setText("\uD83D\uDCC2 Upload");
        this.SettengsButton.setText("⚙ Settings");
        this.scaleText.setText("scale");
        this.DefaultRateLabel.setText("Default Rate");
        this.LexisDiagramLabel.setText("Lexis Diagram");
        this.APCLabel.setText("APC analysis");
        this.goButton.setText("Go");
        this.adjustButton.setText("Adjust");
        this.error.setText("Slope");
        this.featureLabel.setText("Feature");
        this.conditionLabel.setText("Condition");
        this.valueLabel.setText("Value");
        this.ageeffectID.setText("age effect");
        this.periodeffectID.setText("period effect");
        this.cohorteffectID.setText("cohort effect");
        this.ageID.setText("age");
        this.calID.setText("calendar time");
        this.drAgePredicted.setText("Predicted");
        this.drCalPredicted.setText("Predicted");
        this.preAPCID.setText("APC by predicted data");
        this.realAPCID.setText("APC by real data");
        this.realID.setText("real data");
    }

    /**
     * Set language as Chinese
     */
    private void setChinese() {
        this.title.setText("信用风险可视化");
        this.uploadDataButton.setText("\uD83D\uDCC2 上传");
        this.SettengsButton.setText("⚙ 设置");
        this.scaleText.setText("比例");
        this.DefaultRateLabel.setText("违约率");
        this.LexisDiagramLabel.setText("Lexis 图");
        this.APCLabel.setText("APC 分析");
        this.goButton.setText("确认");
        this.adjustButton.setText("调整");
        this.error.setText("误差");
        this.featureLabel.setText("特征");
        this.conditionLabel.setText("条件");
        this.valueLabel.setText("数值");
        this.ageeffectID.setText("年龄效应");
        this.periodeffectID.setText("时期效应");
        this.cohorteffectID.setText("队列效应");
        this.ageID.setText("年龄");
        this.calID.setText("日历时间");
        this.drAgePredicted.setText("预测");
        this.drCalPredicted.setText("预测");
        this.preAPCID.setText("基于预测数据的APC");
        this.realAPCID.setText("基于实际数据的APC");
        this.realID.setText("实际数据");

    }



    /**
     * initialize token string
     * @param filename
     */
    public void initializeToken(String filename){
        try {
            File myObj = new File(filename);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                this.token = data;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    /**
     * Send request to update Graph.
     * @param isDark Whether user open color vision defenciency
     * @param filename filename of database
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    public void updateGraph(boolean isDark,String filename,String token) 
            throws MalformedURLException {
        loadingPane.setVisible(true);
        Duration duration = Duration.millis(2000);
        //Create new rotate transition
        RotateTransition rotateTransition = new RotateTransition(
                duration, loadingImage);
        //Rotate by 360 degree
        rotateTransition.setByAngle(360);
        rotateTransition.play();
        LoadGraphAPI.load("http://127.0.0.1:8000/api/v4/download_graph/",
                token, filename,
                isDark,scenes.getColorVision(),scenes.getError(),
                scenes.getFeature(),scenes.getCondition(),scenes.getValue(),
                scenes.getDecimal(),scenes.getSeparator(),scenes.getAge(),
                scenes.getAgeUnit(),scenes.getCohort(), scenes.getCohortUnit(),
                scenes.getDefaultFlag(),scenes.getPredictedDefaultRate(),
                scenes.getLanguage());
        rotateTransition.setOnFinished(e -> {
            try {
                loadGraph();
            } catch (MalformedURLException ex) {
                throw new RuntimeException(ex);
            }
            loadingPane.setVisible(false);
        });
    }

    /**
     * Load graph from local file.
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    public void loadGraph() throws MalformedURLException {
        drAgewebEngine = drAgeWebView.getEngine();
        File drAgeFile = new File("res\\" +
                scalePrefix + "dr_age.html");
        drAgewebEngine.load(drAgeFile.toURI().toURL().toString());

        drCalwebEngine = drCalWebView.getEngine();
        File drCalFile = new File("res\\" +
                scalePrefix + "dr_cal.html");
        drCalwebEngine.load(drCalFile.toURI().toURL().toString());

        updateTheme(scenes.getIsDark());

        loadAPCGraph();
    }


    /**
     * Load graph from local file for APC analysis.
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    public void loadAPCGraph() throws MalformedURLException {
        ageEngine = ageEffectWebView.getEngine();
        File ageEffectDiagram = new File("res\\" 
                + scalePrefix + "ageeffect.html");
        ageEngine.load(ageEffectDiagram.toURI().toURL().toString());

        periodEngine = periodEffectWebView.getEngine();
        File periodEffectDiagram = new File("res\\" 
                + scalePrefix + "periodeffect.html");
        periodEngine.load(periodEffectDiagram.toURI().toURL().toString());

        cohortEngine = cohortEffectWebView.getEngine();
        File cohortEffectDiagram = new File("res\\" 
                + scalePrefix + "cohorteffect.html");
        cohortEngine.load(cohortEffectDiagram.toURI().toURL().toString());
    }

    /**
     * Update theme
     * @param isDark whether user turn on color vesion defenciency
     * @throws MalformedURLException Thrown to indicate that a malformed URL 
     *              has occurred. Either no legal protocol could be found in a 
     *              specification string or the string could not be parsed.
     */
    public void updateTheme(boolean isDark) throws MalformedURLException {
        if(scenes.getColorVision() == "full"){
            theme.setPromptText("greys");
            realAPCtheme.setPromptText("greys");
            APCtheme.setPromptText("greys");

            lexisDiagramEngine = lexisDiagramWebView.getEngine();
            File lexisDiagram = new File("res\\" 
                   + scalePrefix + "lexis_diagram_greys.html");
            lexisDiagramEngine.load(lexisDiagram.toURI().toURL().toString());

            apcLexisDiagramEngine = APClexisDiagramWebView.getEngine();
            File apcLexisDiagram = new File("res\\" 
                   + scalePrefix + "apc_lexis_diagram_greys.html");
            apcLexisDiagramEngine.load(
                    apcLexisDiagram.toURI().toURL().toString());

            realAPCLexisDiagramEngine = realAPClexisDiagramWebView.getEngine();
            File realApcLexisDiagram = new File("res\\" 
                   + scalePrefix + "real_apc_lexis_diagram_greys.html");
            realAPCLexisDiagramEngine.load(
                    realApcLexisDiagram.toURI().toURL().toString());
        } else if (scenes.getColorVision() != "None") {
            theme.setPromptText("greens");
            realAPCtheme.setPromptText("greens");
            APCtheme.setPromptText("greens");

            lexisDiagramEngine = lexisDiagramWebView.getEngine();
            File lexisDiagram = new File("res\\" 
                   + scalePrefix + "lexis_diagram_greens.html");
            lexisDiagramEngine.load(lexisDiagram.toURI().toURL().toString());

            apcLexisDiagramEngine = APClexisDiagramWebView.getEngine();
            File apcLexisDiagram = new File("res\\" 
                   + scalePrefix + "apc_lexis_diagram_greens.html");
            apcLexisDiagramEngine.load(apcLexisDiagram.toURI().toURL().toString());

            realAPCLexisDiagramEngine = realAPClexisDiagramWebView.getEngine();
            File realApcLexisDiagram = new File("res\\" 
                   + scalePrefix + "real_apc_lexis_diagram_greens.html");
            realAPCLexisDiagramEngine.load(
                    realApcLexisDiagram.toURI().toURL().toString());
        } else {
            theme.setPromptText("hot");
            realAPCtheme.setPromptText("hot");
            APCtheme.setPromptText("hot");

            lexisDiagramEngine = lexisDiagramWebView.getEngine();
            File lexisDiagram = new File("res\\" 
                   + scalePrefix + "lexis_diagram_hot_r.html");
            lexisDiagramEngine.load(
                    lexisDiagram.toURI().toURL().toString());

            apcLexisDiagramEngine = APClexisDiagramWebView.getEngine();
            File apcLexisDiagram = new File("res\\" 
                   + scalePrefix + "apc_lexis_diagram_hot_r.html");
            apcLexisDiagramEngine.load(
                    apcLexisDiagram.toURI().toURL().toString());

            realAPCLexisDiagramEngine = realAPClexisDiagramWebView.getEngine();
            File realAPCLexisDiagram = new File("res\\" 
                   + scalePrefix + "real_apc_lexis_diagram_hot_r.html");
            realAPCLexisDiagramEngine.load(
                    realAPCLexisDiagram.toURI().toURL().toString());
        }

    }

    


    /**
     * Initialize when get dashboard controller.
     * @throws MalformedURLException  Thrown to indicate that a malformed URL has occurred.
     *              Either no legal protocol could be found in a specification string
     *              or the string could not be parsed.
     */
    @FXML
    public void initialize() throws MalformedURLException {
        initializeToken("res\\" + scalePrefix + "token.txt");
        DefaultRatePane.setVisible(true);
        LexisDiagramPane.setVisible(false);
        APCPane.setVisible(false);
        infoPane.setVisible(false);
        WebEngine e= drAgeWebView.getEngine();
        loadingPane.setVisible(false);
    }


}




