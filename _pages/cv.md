---
layout: personal
title: "个人简历"
eyebrow: "CURRICULUM VITAE"
permalink: /cv/
description: "陈亮吉 · Liangji Chen｜南京理工大学数学博士生"
redirect_from:
  - /resume
  - /resume/
---
<div class="cv-toolbar"><a class="text-link" href="mailto:{{ site.data.profile.email }}">{{ site.data.profile.email }}</a><button class="button button-secondary" type="button" data-print hidden>打印 / 保存 PDF <span aria-hidden="true">↗</span></button></div>

<div class="cv-document">
<section class="content-section first-section"><h2>个人简介</h2><p>{{ site.data.profile.intro }}</p><p>职业兴趣：AI 数据算法工程师、数据科学家。</p><p class="print-contact">学术邮箱：{{ site.data.profile.email }}<br>GitHub：{{ site.data.profile.github }}</p></section>
<section class="content-section"><h2>教育背景</h2>{% include profile/education.html %}</section>
<section class="content-section"><h2>实习经历</h2>{% include profile/internships.html %}</section>
<section class="content-section"><h2>项目经历</h2><article class="experience-item"><div class="item-heading"><h3>基于神经网络的电力系统负荷预测</h3><span class="item-date">2023.07 — 2024.07</span></div><p class="item-subtitle">主要负责人</p><p>设计 WT-CNN-LSTM 混合预测框架，结合信号去噪、非线性特征提取与时序建模；完成与传统模型的对照实验，预测误差降低 76.9%。成果发表于《新型工业化》。</p></article><article class="experience-item"><div class="item-heading"><h3>数据交易优化探究</h3><span class="item-date">2023.07 — 2023.09</span></div><p class="item-subtitle">项目成员</p><p>重构“寻源询价”匹配算法，开展与线下磋商模式的对照实验。项目报告与论文入选 DataOps 全球峰会谷雨专家内部推荐。</p></article><a class="text-link cv-project-link" href="{{ '/projects/' | relative_url }}">查看项目详情 <span aria-hidden="true">→</span></a></section>
<section class="content-section"><h2>学术论文</h2><p><strong>陈亮吉</strong>，朱晨君．基于 WT-CNN-LSTM 混合神经网络的电力系统负荷预测模型[J]．新型工业化，2024，14(07)：132–141。</p></section>
<section class="content-section"><h2>校园经历</h2><div class="item-heading"><h3>{{ site.data.profile.campus.organization }} · {{ site.data.profile.campus.role }}</h3><span class="item-date">{{ site.data.profile.campus.period }}</span></div><p>{{ site.data.profile.campus.detail }}</p></section>
<section class="content-section"><h2>竞赛荣誉</h2>{% include profile/awards.html %}</section>
<section class="content-section"><h2>专业技能</h2>{% include profile/skills.html %}</section>
</div>
