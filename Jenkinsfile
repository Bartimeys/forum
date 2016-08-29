node {
  stage 'git'
  git url: 'https://github.com/Bartimeys/forum/tree/FRM-12_integration_to_jenkins'
  
  stage 'install'
  sh "make install"
  
  stage "flake8"
  sh "make flake8"
}
