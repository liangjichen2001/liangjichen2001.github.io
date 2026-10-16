# 陈亮吉的个人主页

这是基于 Academic Pages / Jekyll 的个人网站，内容以中文为主，保留英文姓名与学术术语。

## 修改内容

| 内容 | 文件 |
| --- | --- |
| 姓名、联系信息、教育、实习、荣誉、技能 | `_data/profile.yml` |
| 顶部导航 | `_data/navigation.yml` |
| 网站标题、域名、搜索摘要 | `_config.yml` |
| 首页 | `_pages/about.md` |
| 研究与论文 | `_pages/research.html` |
| 项目详情 | `_pages/portfolio.html`，访问路径 `/projects/` |
| 经历 | `_pages/experience.html` |
| 在线简历 | `_pages/cv.md` |
| 论文条目 | `_publications/2024-07-01-wt-cnn-lstm.md` |
| 论文引用 | `files/chen-2024-load-forecasting.bib` |
| 照片 | `images/liangji-chen.jpg` |
| 视觉样式与打印排版 | `assets/css/personal.css` |
| 深浅色切换、打印按钮 | `assets/js/personal.js` |

教育、实习等多处共用的内容从 `profile.yml` 读取，修改一次即可更新。项目介绍及其数字也出现在首页和简历中，修改成果时请同步对应页面。邮箱沿用原网站的学校邮箱。

简历页面的“打印 / 保存 PDF”按钮调用浏览器打印，可在打印窗口中选择保存为 PDF。公开版本包含学术联系信息；原始求职简历中的电话、出生年月等个人信息未加入网站。照片从所提供简历中提取。

原模板的示例论文、教学、演讲、博客和示例附件保留在源码中，通过 `_config.yml` 的 `exclude` 排除，不会出现在生成网站、订阅或站点地图中。新增正式论文时，请使用新文件名，不要直接编辑已被排除的示例文件。

## 本地预览

安装 Ruby 3.3 与 Bundler 后，在仓库根目录运行（Windows 请使用带 Devkit 的 RubyInstaller，以便编译依赖）：

```powershell
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

访问 `http://127.0.0.1:4000`。修改 `_config.yml` 后需要重启服务。

本次验证所用便携版 Ruby 和检查依赖位于已忽略的 `local/` 目录；不需要将它们提交到 Git。若保留了该目录，也可用以下命令启动：

```powershell
$env:PATH = "$PWD\local\rubyinstaller-3.3.7-1-x64\bin;$env:PATH"
bundle exec jekyll serve --host 127.0.0.1
```

构建与站内链接检查：

```powershell
bundle exec jekyll build --strict_front_matter
python scripts/check_site.py _site
```

## 发布至 GitHub Pages

仓库已包含 `.github/workflows/jekyll.yml`，在推送至 `master` 后构建并部署。

1. 在 GitHub 仓库的 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
2. 将本地更改提交并推送到 `master`。
3. 在 **Actions** 查看 **Deploy personal website to GitHub Pages** 的运行结果。
4. 成功后访问 `https://liangjichen2001.github.io/`。

部署流程会先构建网站并检查页面、站内链接及锚点，通过后才发布。PR 会执行构建检查。源码中的上游模板 PR 清理工作流已限制为只在上游模板仓库运行。

GitHub Pages 配置说明：https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
