node {
  stage 'git'
  git branch: 'FRM-12_integration_to_jenkins', url: 'https://github.com/Bartimeys/forum'
  
  stage 'install'
  sh "make install"
  
  stage "flake8"
  sh "make flake8"
}
