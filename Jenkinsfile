node {
  stage 'git'
  git branch: BRANCH_NAME, url: 'https://github.com/Bartimeys/forum'
  
  stage 'install'
  sh "make install"
  
  stage "flake8"
  sh "make flake8"
}
