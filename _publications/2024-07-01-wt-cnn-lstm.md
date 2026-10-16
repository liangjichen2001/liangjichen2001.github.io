---
layout: personal
title: "基于 WT-CNN-LSTM 混合神经网络的电力系统负荷预测模型"
eyebrow: "JOURNAL ARTICLE / 2024"
collection: publications
category: manuscripts
permalink: /publication/2024-wt-cnn-lstm/
date: 2024-07-01
venue: "新型工业化"
volume_issue: "14(07)"
pages: "132–141"
bibtexurl: /files/chen-2024-load-forecasting.bib
description: "陈亮吉、朱晨君发表于《新型工业化》的电力系统负荷预测研究，结合小波变换与 CNN-LSTM 混合神经网络。"
---

<div class="paper-metadata"><p><strong>陈亮吉</strong>，朱晨君</p><p>《新型工业化》，2024 年，14(07)：132–141</p><a class="button button-secondary" href="{{ page.bibtexurl | relative_url }}" download>下载 BibTeX <span aria-hidden="true">↓</span></a></div>

## 研究概述

针对传统电力负荷预测模型精度不足、抗干扰性弱的问题，本研究将小波变换与 CNN-LSTM 神经网络结合，构建混合预测框架。通过过滤原始负荷数据中的噪声，提升模型对非线性特征与时间依赖的捕捉能力。

## 方法与实验

- **小波变换（WT）**：处理原始负荷信号中的噪声干扰。
- **卷积神经网络（CNN）**：提取负荷数据中的局部与非线性特征。
- **长短期记忆网络（LSTM）**：学习时间序列的依赖关系，完成负荷预测。
- **对照实验**：与传统机器学习模型、单结构预测模型进行多维度性能比较。在本项目实验中，相较于传统模型，预测误差降低 76.9%。

## 引用

> 陈亮吉，朱晨君．基于 WT-CNN-LSTM 混合神经网络的电力系统负荷预测模型[J]．新型工业化，2024，14(07)：132–141。

<a class="text-link" href="{{ '/projects/#load-forecasting' | relative_url }}">查看项目背景 <span aria-hidden="true">→</span></a>
