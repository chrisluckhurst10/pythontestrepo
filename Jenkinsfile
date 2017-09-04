#!/usr/bin/env groovy

import groovy.io.FileType;
import hudson.FilePath;
import java.io.File;
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
    writeFile file: "output/uselessfile.md", text: "This file is useless, no need to archive it"
    
    stage "Archive build output"
    
    archiveArtifacts artifacts: 'output/*.txt', excludes: 'output/*.md'
    //    }
    //}
}
