package edu.gt.cs4567.hw1;

import org.apache.lucene.analysis.standard.StandardAnalyzer;

public class App {
    public static void main(String[] args) {
        StandardAnalyzer analyzer = new StandardAnalyzer();
        System.out.println("Lucene is working");
    }
}
