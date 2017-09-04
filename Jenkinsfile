#!/usr/bin/env groovy

pipeline {
    agent any 
    
    node {
        stage "Create output build"
            //make an output directory
        sh "mkdir -p output"
            
            //write a useful output file, which needs to be archived
        writeFile file: "output/usefulfile.txt", text: "This file is useful, need to archive it"
            
            //write a useless output file, which doesn't need to be archived
        writeFile file: "output/uselessfile.md"
    }
}
