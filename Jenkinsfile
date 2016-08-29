node {
  stage 'git'
  checkout scm
  
  stage 'install'
  sh "make install"
  
  stage "flake8"
  //sh "make flake8"
  echo 'ok'
  
  stage "tests"
  sh "make tests"
}
