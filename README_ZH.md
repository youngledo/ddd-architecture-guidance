# 领域架构插件

中文 ｜ [英文](README.md)

---

面向业务领域软件系统的插件优先架构指导包。它帮助人工智能编程智能体从业务需求走到领域模型、架构决策，并在适用时提供框架落地指导；不会把 DDD、六边形架构、洋葱架构、CQRS 或某个框架约定混成一套强制组合模型。

## 快速开始

### Codex

```bash
codex plugin marketplace add xfoundries/domain-architecture-skills
codex plugin add domain-architecture@xfoundries
```

通过 `codex plugin list` 确认插件已出现，然后直接发送：

```text
请将 $domain-architecture-workflow 用于这个业务项目。

业务目标与已知规则：
现有项目或产物：
技术约束：
是否使用 jfoundry：是 | 否 | 未决定
期望的下一步活动：
```

工作流会利用已有证据，只询问阻碍负责决策的事实，并返回适用的专业结果和供规划、实施或评审使用的 `Domain Architecture Handoff`。

如果从当前检出目录做本地开发，改用本地来源：

```bash
codex plugin marketplace add .
codex plugin add domain-architecture@xfoundries
```

`xfoundries` 市场名称只能对应一个来源。要在本地检出与 Git 来源之间切换，先移除已有市场：

```bash
codex plugin marketplace remove xfoundries
```

### Claude Code 与兼容的智能体

Claude Code 可以校验并安装同一个插件源码：

```bash
claude plugin validate .
claude plugin marketplace add xfoundries/domain-architecture-skills
claude plugin install domain-architecture@xfoundries
```

仓库还提供适用于兼容智能体的 [`.agents/plugins` 市场清单](.agents/plugins/marketplace.json)。`skills/` 是插件内部能力，应安装 `domain-architecture` 插件，而非单独复制技能。

## 它能做什么

端到端任务从 `domain-architecture-workflow` 开始：

```text
需求
-> 领域建模
-> 架构指导
-> 可选的 jfoundry 落地
-> Domain Architecture Handoff
-> 详细规划或用户选定的流程伴侣
```

交接会保留专业结果、决策、约束、开放问题和阻塞项，并标明最小的规划就绪增量及其下一步所有者；它是规划输入，不是详细实施计划。工作流支持带版本的机器可读交接契约，其中包含稳定身份、修订版本、按依赖范围划分的阻塞项、产物引用、带接受证据的假设以及规划就绪元数据。Markdown 仍然是便于人工评审的投影，已有只理解文本交接的消费方仍可兼容。持久化的工作流产物位于 `docs/domain-architecture/`，独立详细计划位于其 `plans/` 子目录。

| 需求 | 入口 |
|---|---|
| 端到端的业务领域分析与交接 | `domain-architecture-workflow` |
| 有范围的战略与战术建模：业务能力、子域、限界上下文、上下文映射、现状/目标语义冲突、业务规则、生命周期和战术模式 | `domain-modeling` |
| 架构决策或边界评审 | `domain-architecture-guidance` |
| 已确认的 jfoundry 实现落地 | `using-jfoundry` |

`domain-modeling` 仅在待决策问题确实需要时启用战略建模，例如系统拆分、多团队责任归属或跨上下文语义冲突。已建立限界上下文内的增量可以只做战术建模，也可以返回轻量的 `not-applicable` 结果。战略建模描述业务问题空间，不会据此推导团队、模块、微服务、数据库、部署边界或架构风格。

## 适用范围与限制

- 核心领域建模和架构指导方法与语言、框架无关，但 Java/Kotlin 的实现指导最深入。C#/.NET、Go、Python 提供生态映射而非代码模板；`using-jfoundry` 仅适用于 Java。
- 主要面向业务后端软件。客户端在拥有实质业务行为、离线工作流、同步冲突或本地持久化边界时可按需使用；本插件不提供移动端或前端平台的专项实现模板。
- 领域建模可以区分业务能力、子域、限界上下文和上下文映射，也能表达棕地系统中的现状与目标语义。它只按当前决策所需的深度记录业务规则、生命周期转换、不变量、聚合及其他战术模式。
- 不要把 DDD、端口与适配器、CQRS、仓储或分层架构强行套到简单 CRUD、薄客户端或小脚本中。

## 进阶使用

- 只有在确认或明确要求 jfoundry 时才使用 `using-jfoundry`；框架尚未决定不会阻塞框架中立的领域建模和架构指导。其[架构落地说明](skills/using-jfoundry/references/architecture.md)保留已选架构风格，而不是替项目选择一种风格。
- Superpowers、SpecKit、OpenSpec 等流程伴侣是可选且由用户选择的。它们拥有自身的规格、规划、任务、实施、评审、文件和命令；本插件拥有专业结果和交接。[首次使用指南](skills/domain-architecture-workflow/references/first-use.md)定义了输入、责任归属、状态和返回规则。
- 结构化交接契约以增量方式加入，不改变专业结果的所有权，也不要求工作流引擎。仓库现在提供基于标准库的交接校验、阻塞项解决后生成新修订版本，以及摘要/完整 Markdown 投影工具；数据库持久化和分布式恢复仍不在当前阶段。当前契约见 [handoff-contract.md](skills/domain-architecture-workflow/references/handoff-contract.md)，其 JSON Schema 见[这里](schemas/domain-architecture-handoff.schema.json)。
- 交接消费方可以请求摘要或完整投影。持久化产物可以声明敏感性分类和脱敏要求；流程伴侣消费契约和引用，但仍然拥有自己的规划与执行状态。
- 已选择的架构风格保留自身约束。聚合仓储、适配器词汇、集成契约和可靠消息应遵循[架构约束](skills/domain-architecture-guidance/references/architecture-constraints.md)及适用的专业参考资料；插件不会根据包名或可用框架能力推断这些选择。

## 资料来源策略

架构指导把资料分为三层：

- 基础来源：Eric Evans 用于 DDD，Alistair Cockburn 用于 Hexagonal Architecture，Martin Fowler 用于企业应用模式和 CQRS 讨论，Greg Young 用于 CQRS，Jeffrey Palermo 用于 Onion Architecture，Clean Architecture 只谨慎用于依赖方向综合。
- 广泛使用的实现指导：jMolecules、Microsoft .NET 架构指导、Spring Modulith、ArchUnit、ArchUnitNET、microservices.io。
- 带个人观点的综合模型和示例：可以参考，但不能作为权威标准。

这个插件区分 DDD 建模概念、架构风格约束和框架约定，不会把 DDD、分层架构、洋葱架构、六边形架构、CQRS 和事件溯源表述成一个标准架构。

## 仓库结构

```text
.codex-plugin/
  plugin.json
.claude-plugin/
  marketplace.json
  plugin.json
.agents/plugins/
  marketplace.json
skills/
  domain-architecture-workflow/
  domain-modeling/
  domain-architecture-guidance/
  using-jfoundry/
```

## 更新

本地开发时，保持目标智能体的 marketplace 源指向本仓库即可。修改插件元数据后，在目标智能体中重新安装或更新插件，让它刷新缓存。

Codex 与 Claude 清单共享同一个 SemVer 发布版本。向后兼容的新能力递增 `MINOR`，兼容性修复递增 `PATCH`；`1.0.0` 之后的不兼容公共契约变更递增 `MAJOR`，`1.0.0` 之前则递增下一个 `MINOR`。发布标签使用 `domain-architecture--v<version>`。

Codex 的 `.codex-plugin/plugin.json` 会在发布版本后追加 `+codex.<cachebuster>`。当插件内容或元数据变化并需要使 Codex 缓存失效时，只刷新该后缀；不要仅为刷新缓存而递增发布版本。之后从 `domain-architecture@xfoundries` 重新安装。

## 设计原则

用架构模式保护业务含义和变化边界，不要把它们当成装饰性目录结构。
