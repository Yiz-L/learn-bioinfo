@echo off
chcp 65001 >/dev/null
echo ====================================
echo  部署编程学习网站到 GitHub Pages
echo ====================================
echo.

cd /d D:\Desk\编程入门

echo 第1步：初始化 Git 仓库...
git init

echo 第2步：添加所有文件...
git add .

echo 第3步：首次提交...
git commit -m "🎉 初始化：医学僧编程学习路径网站"

echo 第4步：创建 GitHub 仓库并推送...
gh repo create learn-bioinfo --public --push --source=.

echo 第5步：部署到 GitHub Pages...
mkdocs gh-deploy --force

echo.
echo ====================================
echo  ✅ 部署完成！
echo ====================================
echo  你的网站将在1-2分钟后上线：
echo  https://yizl.github.io/learn-bioinfo/
echo.
pause
