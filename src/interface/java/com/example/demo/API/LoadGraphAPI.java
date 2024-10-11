package com.example.demo.API;

import java.io.*;
import java.net.*;
/***
 import java.net.MalformedURLException;
 import java.net.URL;
 import java.net.URLConnection;
 import java.net.http.HttpClient;
 import java.net.HttpURLConnection;
 ***/


public class LoadGraphAPI {
    private static HttpURLConnection connection;

    /**
     * Load graph.
     * @param urlLink url link.
     * @param token strings of tokens.
     * @param filename filename of database.
     * @param isDark whether user turn on color vision deficiency.
     * @param error error value.
     * @param feature feature for condition.
     * @param condition < or >.
     * @param value value.
     * @param separator value of separator for svm file.
     * @param age title of age.
     * @param ageUnit title of age unit.
     * @param cohort title of cohort.
     * @param cohortUnit title of cohort unit.
     * @param defaultFlag title of default flag.
     * @param predictedDefaultTitle title of predicted default rate.
     */
    public static void load(String urlLink, String token, String filename,
                            boolean isDark,String colorVision, String error,
                            String feature, String condition, String value,
                            String decimal, String separator, String age,
                            String ageUnit, String cohort, String cohortUnit,
                            String defaultFlag, String predictedDefaultTitle,
                            String language){
        String token_string = "Token " + token;
        try{
            URL url = new URL(urlLink);
            connection = (HttpURLConnection) url.openConnection();

            connection.setRequestMethod("POST");
            connection.setRequestProperty("Authorization",token_string);

            System.out.println();
            String requestBody = "filename=" + filename + "&isDark=" 
                    + String.valueOf(isDark) + "&colorVision=" 
                    + colorVision + "&error=" + error+ "&feature=" + feature 
                    + "&condition=" + condition + "&value=" + value 
                    + "&decimal=" + decimal +"&separator=" + separator 
                    + "&ageTitle=" + age + "&ageUnit=" + ageUnit 
                    + "&cohortTitle=" + cohort + "&cohortUnit=" 
                    + cohortUnit + "&defaultFlagTitle=" + defaultFlag 
                    + "&predictedDefaultTitle=" + predictedDefaultTitle
                    + "&language=" + language;
            System.out.println(requestBody);
            connection.setDoOutput(true);
            OutputStream outputStream = connection.getOutputStream();
            outputStream.write(requestBody.getBytes());
            outputStream.flush();
            outputStream.close();

            //get response code
            int status = connection.getResponseCode();
            System.out.println(status);


        } catch (MalformedURLException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            connection.disconnect();
        }

    }


}
