#!/usr/bin/env groovy

import com.tikal.jenkins.plugins.multijob.MultiJobBuild.SubBuild;
import hudson.FilePath;
import java.io.Writer.write;
import jenkins.model.Jenkins;

//pipeline {
//    agent any 
    
//    stages {
node {
    stage "Create output build"
            //make an output directory
    sh "mkdir -p output"
            
            //write a useful output file, which needs to be archived
    writeFile file: "output/usefulfile.txt", text: "This file is useful, need to archive it"
            
            //write a useless output file, which doesn't need to be archived
    writeFile file: "output/uselessfile.md"
    //    }
    //}
}
