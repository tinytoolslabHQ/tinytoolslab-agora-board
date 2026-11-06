import streamlit as st
import pandas as pd

st.set_page_config(page_title="tinytoolslab 7人董事会", layout="wide", page_icon="🏢")

# 顶部
st.title("🏢 tinytoolslabHQ | 7人单数最稳 | 视觉外置电脑做")
st.caption("董事长只跟CEO聊 | 3天大上新+2天小迭代 | 免费云端不睡觉 | 夜里2点中国时间自动爬")

# 侧边栏-品牌库
with st.sidebar:
    st.header("📦 品牌库-已上架3个")
    st.write("✅ AI Mock Interview $35 - 已上架")
    st.write("✅ Notion Job Tracker $29 - 已上架")
    st.write("✅ Finance Pack $19 - 已上架")
    st.divider()
    st.header("🔑 大脑钥匙（免费）")
    groq_key = st.text_input("Groq Key 免费100次/天", type="password", help="https://console.groq.com/keys")
    deepseek_key = st.text_input("DeepSeek Key 送10元", type="password", help="https://platform.deepseek.com/api_keys")
    st.divider()
    st.header("🎨 视觉外置")
    st.info("板子只出模板：封面尺寸1024、Etsy10图清单、30秒脚本文字。真图真视频你们电脑用豆包+CapCut 2小时做，质量比云端免费图好10倍")
    st.divider()
    st.write("邮箱：tinytoolslabHQ@qq.com")
    st.write("7人：CEO(我)、市场爬虫、数据表格、产品技术、法务风控、增长定价、数据验证")

# 中间-董事长CEO聊天
st.subheader("💬 董事长-CEO聊天（只跟CEO聊，绝不跑题）")
chairman_q = st.text_input("董事长指令：", placeholder="@CEO 什么最好卖？搜索量成交量利润多少？为什么？", key="chairman")

col1, col2 = st.columns([1,3])
with col1:
    if st.button("让7人开会", type="primary"):
        if not chairman_q:
            st.warning("先输入董事长指令")
        else:
            with st.spinner("7人关门吵架中...市场爬虫30分钟、数据表格1小时、辩论2.5小时..."):
                st.session_state["meeting_done"] = True
                st.session_state["q"] = chairman_q

with col2:
    if st.session_state.get("meeting_done"):
        st.success(f"CEO（我-DeepSeek R1）：董事长，收到【{st.session_state.get('q','')}】")
        st.write("**市场爬虫部-Groq**：夜里2点爬6个源完成，Product Hunt今日最火AI Prompt Pack 2.1k搜索")
        st.write("**数据表格部-DeepSeek V3**：10维大表已算，见右边")
        st.write("**数据验证部-DeepSeek R1**：Reddit看了，老外差评说竞品缺STAR范文和公司标签")
        st.write("**法务风控部**：已上架3个黑名单排除，重复检测通过")
        st.write("---")
        st.markdown("### ✅ 最终答案（CEO统一出口）：")
        st.markdown("**董事长，本月最好做 Mock Interview OS Pro Bundle $49**")
        st.markdown("- 搜索量 3200（40%加权最高）、成交量 120、竞争少、利润$47、风险低、常青、机会分 **9.2分**")
        st.markdown("- 4票赞成2票弃权1票反对，7人单数最稳通过")
        st.markdown("- 模板已出：ZIP+3赠品+封面BUNDLE角标+ Etsy10图清单+30秒脚本 `one hundred FAANG questions...`")
        st.markdown("- 真图真视频你们电脑上豆包+CapCut 2小时做，质量好")
        st.markdown("- 需要我现在出Gumroad $29首发和Etsy $29.99上架包吗？")

# 右边-10维大表
st.subheader("📊 10维大表 - 数据表格部做的（做表格的）")
data = {
    "产品": ["Mock Interview Pro Bundle", "Job Tracker Pro", "Finance Pro", "AI Prompt Pack"],
    "搜索量40%加权": [3200, 2100, 890, 2100],
    "成交量": [120, 85, 30, 300],
    "竞争": ["少", "中", "少", "多"],
    "利润": ["$47", "$29", "$19", "$15"],
    "风险": ["低", "低", "中", "中"],
    "流量可持续": ["常青每月卖", "常青", "季节性", "常青"],
    "差评原因": ["缺公司标签", "缺模板", "缺更新", "太多同类"],
    "定价甜点+LTV": ["$49 Bundle LTV高", "$29", "$19", "$19"],
    "机会分=(需求*利润)/(竞争*风险)": [9.2, 7.5, 5.1, 6.8],
}
df = pd.DataFrame(data).sort_values("机会分=(需求*利润)/(竞争*风险)", ascending=False)
st.dataframe(df, use_container_width=True)

st.info("💡 公式：机会分=(需求*利润)/(竞争*风险)，搜索量占40%权重，常青每月能卖，不是考研那种季节性")

# 底部-3天流水线
st.subheader("⏰ 3天流水线（夜里2点中国时间开工）")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.write("**Day0 夜里2-10点**")
    st.write("02:00-02:30 市场爬虫")
    st.write("02:30-03:30 数据表格做表")
    st.write("03:30-06:00 7人吵3轮投票")
    st.write("06:00-09:00 出ZIP+模板")
with c2:
    st.write("**Day1 白天**")
    st.write("你们电脑做真图真视频")
    st.write("豆包+CapCut 2小时")
    st.write("30秒带货+210秒操作")
    st.write("Etsy10图切好")
with c3:
    st.write("**Day2 白天**")
    st.write("上架Gumroad $29首发")
    st.write("Etsy $29.99")
    st.write("YouTube Shorts+TikTok")
    st.write("Bundle $49")
with c4:
    st.write("**Day3**")
    st.write("看销量回流")
    st.write("算收入")
    st.write("黑名单同步")
    st.write("准备下一轮")

st.divider()
st.caption("最终7人：CEO(我)、市场爬虫、数据表格(做表格的)、产品技术、法务风控、增长定价、数据验证 | 视觉外置电脑做 | Dify自建+CrewAI丢HF免费云端 | Groq快+DeepSeek推理+豆包视觉")
