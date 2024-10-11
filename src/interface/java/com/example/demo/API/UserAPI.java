package com.example.demo.API;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.URL;
import java.net.URLConnection;


public class UserAPI {
	private String email;
	private String password;

	/**
	 *
	 * param body:should be name1=value1&name2=value2
	 */
	/**
	 * log in to the application.
	 * @param url url link.
	 * @param email email of the user.
	 * @param password password of the user.
	 * @return strings of tokens.
	 */
	public static String login(String url, String email,String password) {
		PrintWriter out = null;
		BufferedReader in = null;
		String result = "";
		String output = "";
		try {
			URL realUrl = new URL(url);
			URLConnection conn = realUrl.openConnection();
			conn.setRequestProperty("accept", "*/*");
			conn.setRequestProperty("connection", "Keep-Alive");
			conn.setRequestProperty("user-agent",
					"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)");
			conn.setDoOutput(true);
			conn.setDoInput(true);
			out = new PrintWriter(conn.getOutputStream());
			String param = "email=" + email + "&password=" + password;
			out.print(param);
			out.flush();
			/***
			in = new BufferedReader(
					new InputStreamReader(conn.getInputStream()));
			//result = in.readLine();
			String line;
			while ((line = in.readLine()) != null) {
				result += line;
			}
			 ***/

			BufferedReader reader = new BufferedReader(
					new InputStreamReader((conn.getInputStream())));
			output = reader.readLine();
			/***
			StringBuffer responseContent = new StringBuffer();
			while((output = reader.readLine()) != null){
				responseContent.append(output);
			}
			 ***/
		} catch (Exception e) {
			System.out.println("Unable to send the request" + e);
			e.printStackTrace();
		}
		finally {
			try {
				if (out != null) {
					out.close();
				}
				if (in != null) {
					in.close();
				}
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
		output = output.substring(2,output.length() - 2);
		return output;
	}


}

