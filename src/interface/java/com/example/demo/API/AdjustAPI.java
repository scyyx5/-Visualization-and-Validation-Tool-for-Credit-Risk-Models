package com.example.demo.API;

import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

/***
 import java.net.MalformedURLException;
 import java.net.URL;
 import java.net.URLConnection;
 import java.net.http.HttpClient;
 import java.net.HttpURLConnection;
 ***/


public class AdjustAPI {
	private static HttpURLConnection connection;
	private String error;

	/**
	 * Send adjust request.
	 * @param urlLink url link.
	 * @param token strings of tokens.
	 * @param filename filename of database.
	 * @param isDark whether user turn on color vision deficiency.
	 * @param error error value.
	 */
	public static void adjustAPC(String urlLink, String token, String filename,
								 boolean isDark, String error,String feature,
								 String condition, String value, String ageUnit,
								 String cohortUnit,String decimal, String separator){
		String tokenString = "Token " + token;
		try{
			URL url = new URL(urlLink);
			connection = (HttpURLConnection) url.openConnection();

			//request setup
			connection.setRequestMethod("POST");
			connection.setRequestProperty("Authorization",tokenString);

			String requestBody = "filename=" + filename + "&isDark="
					+ String.valueOf(isDark) + "&error=" + error + "&feature="
					+ feature + "&condition=" + condition + "&value=" + value
					+ "&ageUnit=" + ageUnit + "&cohortUnit=" + cohortUnit
					+ "&decimal=" + decimal +"&separator=" + separator;
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

	/**
	 * Send adjust request.
	 * @param urlLink url link.
	 * @param token strings of tokens.
	 * @param filename filename of database.
	 * @param isDark whether user turn on color vision deficiency.
	 * @param error error value.
	 */
	public static void adjust(String urlLink, String token, String filename, boolean isDark, String error){
		String tokenString = "Token " + token;
		try{
			URL url = new URL(urlLink);
			connection = (HttpURLConnection) url.openConnection();

			//request setup
			connection.setRequestMethod("POST");
			//connection.setConnectTimeout(10000);e
			//connection.setReadTimeout(10000);
			//connection.setRequestProperty("Authorization", "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8");
			connection.setRequestProperty("Authorization",tokenString);

			String requestBody = "filename=" + filename + "&isDark=" + String.valueOf(isDark) + "&error=" + error ;
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
