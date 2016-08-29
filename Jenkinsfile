node {
  stage 'git'
  checkout scm
  
  stage 'install'
  sh "make install"
  
  stage "tests"
  sh "make tests"
  
  stage "flake8"
  sh "make flake8"
}
