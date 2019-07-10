# git学习笔记

### 零、配置用户名和邮箱
* 安装完成后，还需要最后一步设置，在命令行输入：
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "email@example.com"
  ```

### 一、初始化仓库
* 初始化一个Git仓库，使用`git init`命令。
* 添加文件到Git仓库，分两步：  
  1. 使用命令`git add <file>`，注意，可反复多次使用，添加多个文件；  
  2. 使用命令`git commit -m <message>`，完成。

### 二、查看状态
* 要随时掌握工作区的状态，使用`git status`命令。
* 如果`git status`告诉你有文件被修改过，用`git diff`可以查看修改内容。

### 三、版本回退
* HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令`git reset --hard <commit_id>`。
* 穿梭前，用`git log`可以查看提交历史，以便确定要回退到哪个版本。
* 要重返未来，用`git reflog`查看命令历史，以便确定要回到未来的哪个版本。

### 四、工作区和暂存区
* `git add <file>`命令实际上就是把要提交的所有修改放到暂存区（Stage），然后，执行`git commit -m <message>`就可以一次性把暂存区的所有修改提交到分支。

### 五、撤销修改
* 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令`git checkout -- <file>`。
* 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令`git reset HEAD <file>`，就回到了场景1，第二步按场景1操作。
* 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考*版本回退*一节，不过前提是没有推送到远程库。

### 六、删除文件
* 确实要从版本库中删除该文件，那就用命令`git rm <file>`删掉，并且`git commit -m <message>`，文件就从版本库中被删除了。
* 另一种情况是删错了，因为版本库里还有呢，所以可以很轻松地把误删的文件恢复到最新版本：`git checkout -- <file>`。
* `git checkout -- <file>`其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。

### 七、远程仓库
* 创建SSH Key
  ```
  ssh-keygen -t rsa -C "youremail@example.com"
  ```
* 如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。
* 登陆GitHub，打开“Account settings”，“SSH Keys”页面，然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容。 
* mac系统会保存登录的github账号和密码，如果执行`git push origin master`报403错误，可以在`钥匙串访问`app中删除旧账号，再登录新账号和密码即可。
* 如果远程仓库和本地仓库里的文件不一致，需要先执行`git pull origin master`拉取远程仓库中的文件，然后再推送。

### 八、创建与合并分支
* 查看分支：`git branch`
* 创建分支：`git branch <name>`
* 切换分支：`git checkout <name>`
* 创建+切换分支：`git checkout -b <name>`
* 合并某分支到当前分支：`git merge <name>`
* 删除分支：`git branch -d <name>`

### 九、忽略特殊文件
* 忽略某些文件时，需要编写.gitignore。
* .gitignore文件本身要放到版本库里，并且可以对.gitignore做版本管理！
  ```
  .DS_Store
  node_modules/
  /dist/
  npm-debug.log*
  yarn-debug.log*
  yarn-error.log*

  # Editor directories and files
  .idea
  .vscode
  *.suo
  *.ntvs*
  *.njsproj
  *.sln
  ```

