---
layout: personal
permalink: /
title: "个人主页"
description: "陈亮吉，南京理工大学数学博士生。研究兴趣包括计算数学、随机过程与最优搜索、机器学习；具有电力负荷预测、用户流失分析和数据交易优化项目经验。"
home: true
redirect_from:
  - /about/
  - /about.html
---

<section class="home-hero" aria-labelledby="hero-title">
  <p class="eyebrow"><span class="status-dot" aria-hidden="true"></span> MATHEMATICS · DATA · INTELLIGENCE</p>
  <h1 id="hero-title">探索随机性，<br>构建有依据的预测<span class="accent">。</span></h1>
  <p class="hero-intro">你好，我是<strong>陈亮吉</strong>。{{ site.data.profile.intro }}</p>
  <div class="hero-actions"><a class="button button-primary" href="{{ '/projects/' | relative_url }}">浏览我的项目 <span aria-hidden="true">↗</span></a><a class="text-link" href="{{ '/cv/' | relative_url }}">查看个人简历 <span aria-hidden="true">→</span></a></div>
  <div class="hero-topics"><span>随机过程</span><span>最优搜索</span><span>机器学习</span><span>数据科学</span></div>
</section>

<section class="content-section" id="research-interests" aria-labelledby="research-title">
  <div class="section-heading"><h2 id="research-title">研究兴趣</h2><a class="text-link" href="{{ '/research/' | relative_url }}">研究与论文 <span aria-hidden="true">↗</span></a></div>
  <div class="interest-grid">{% for interest in site.data.profile.interests %}<article><span class="section-number">{{ interest.number }}</span><h3>{{ interest.title }}</h3><p>{{ interest.description }}</p></article>{% endfor %}</div>
</section>

<section class="content-section" aria-labelledby="featured-title">
  <div class="section-heading"><h2 id="featured-title">项目精选</h2><a class="text-link" href="{{ '/projects/' | relative_url }}">全部项目 <span aria-hidden="true">↗</span></a></div>
  <article class="featured-project">
    <p class="eyebrow">TIME SERIES / DEEP LEARNING</p>
    <h3><a href="{{ '/projects/#load-forecasting' | relative_url }}">基于混合神经网络的<br>电力系统负荷预测</a></h3>
    <p>将小波变换与 CNN-LSTM 结合，处理负荷数据中的噪声，学习非线性特征与时间依赖。</p>
    <div class="model-flow" aria-label="模型流程：小波变换，卷积神经网络，长短期记忆网络，负荷预测"><span>WT<small>信号去噪</small></span><b aria-hidden="true">→</b><span>CNN<small>特征提取</small></span><b aria-hidden="true">→</b><span>LSTM<small>时序建模</small></span><b aria-hidden="true">→</b><span>预测<small>电力负荷</small></span></div>
    <div class="project-bottom"><p><strong>76.9<span>%</span></strong><span>相较于传统模型的预测误差降幅</span></p><a class="text-link" href="{{ '/projects/#load-forecasting' | relative_url }}">项目详情 <span aria-hidden="true">↗</span></a></div>
  </article>
</section>

<section class="content-section" aria-labelledby="education-title"><div class="section-heading"><h2 id="education-title">教育背景</h2><span class="section-note">EDUCATION</span></div>{% include profile/education.html %}</section>

<section class="content-section" aria-labelledby="publication-title">
  <div class="section-heading"><h2 id="publication-title">学术论文</h2><a class="text-link" href="{{ '/research/#publications' | relative_url }}">查看论文 <span aria-hidden="true">↗</span></a></div>
  {% for publication in site.publications reversed %}<article class="publication-entry"><span class="publication-year">{{ publication.date | date: '%Y' }}</span><div><h3><a href="{{ publication.url | relative_url }}">{{ publication.title }}</a></h3><p><strong>陈亮吉</strong>，朱晨君</p><p class="muted">{{ publication.venue }} · {{ publication.volume_issue }} · {{ publication.pages }}</p></div></article>{% endfor %}
</section>

<section class="content-section" aria-labelledby="experience-title"><div class="section-heading"><h2 id="experience-title">实习经历</h2><a class="text-link" href="{{ '/experience/' | relative_url }}">完整经历 <span aria-hidden="true">↗</span></a></div>{% include profile/internships.html compact=true %}</section>

<section class="contact-panel" aria-labelledby="contact-title"><p class="eyebrow">LET’S CONNECT</p><h2 id="contact-title">交流研究，也探讨实践。</h2><p>欢迎就随机过程、机器学习、数据分析及相关合作与我联系。</p><a href="mailto:{{ site.data.profile.email }}">{{ site.data.profile.email }} <span aria-hidden="true">↗</span></a></section>
