
import streamlit as st

st.title("O QUE O SEU TÊNIS ADIDAS DIZ SOBRE VOCÊ?")

st.markdown("## Descubra a personalidade de cada modelo e veja qual combina mais com você!")

st.markdown("## MODELOS ADIDAS")

st.markdown("#### 1. ADIDAS SAMBA:")
st.image('https://i1.t4s.cz/products/id0478/adidas-originals-samba-og-w-855645-id0478.png')
st.write('-> Você é estiloso(a), clássico(a) e gosta de tendências que nunca saem de moda.')

st.markdown("#### 2. ADIDAS CAMPUS:")
st.image('https://speedoutletsneakers.com.br/cdn/shop/files/1_9f759f2f-05b7-40fa-8de3-20795b9ab5ff.webp?v=1685379391')
st.write('-> Você tem vibe tranquila, moderna e curte um estilo casual sem esforço.')

st.markdown("#### 3. ADIDAS GAZELLE:")
st.image('https://www.hypeconcept.com.br/cdn/shop/files/0B23D412-0D44-4989-B271-E11DC39A8775_750x.webp?v=1726892624')
st.write('-> Você gosta de peças icônicas, tem personalidade forte e ótimo gosto.')

st.markdown("#### 4. ADIDAS FORUM:")
st.image('https://cdn.vnda.com.br/780x/pardalsneakers/2023/08/21/22_11_47_284_tenis_adidas_forum_low_yoyogi_park_3477_1_8f30dc8df5335ddd4ccc18010fdc4291.png?v=1692666707')
st.write('-> Você curte referências retrô, atitude urbana e presença marcante.')

st.markdown("#### 5. ADIDAS SUPERSTAR:")
st.image('https://cdn.vnda.com.br/780x/pardalsneakers/2023/08/21/22_10_40_457_tenis_adidas_superstar_gold_metallic_1475_1_d1a393c1c47f652bb35f65f25385a855_20210812081442.png?v=1692666640')
st.write('-> Você é confiante, gosta de chamar atenção e valoriza clássicos lendários.')

st.markdown("#### 6. ADIDAS NMD:")
st.image('https://image.goat.com/transform/v1/attachments/product_template_pictures/images/104/024/891/original/IE9076.png.png?action=crop&width=750')
st.write('-> Você prioriza conforto, tecnologia e vive sempre em movimento.')

st.markdown("#### 7. ADIDAS ULTRABOOST:")
st.image('https://cdn.vnda.com.br/780x/pardalsneakers/2023/08/21/22_10_49_241_tenis_adidas_ultraboost_20_city_pack_sydney_1767_1_fa67e1d2dc0b81c60998740f51363015_20210812081452.png?v=1692666649')
st.write('-> Você gosta de performance, qualidade premium e estar sempre um passo à frente.')

# Parte 2 - Interação

st.markdown("---")
st.markdown("## DESCUBRA O SEU")

opcao = st.selectbox(
    "Escolha seu modelo favorito:",
    ["Samba", "Campus", "Gazelle", "Forum", "Superstar", "NMD", "Ultraboost"]
)

if opcao == "Samba":
    st.success("Você é clássico e estiloso.")
elif opcao == "Campus":
    st.success("Você é criativo, leve e casual.")
elif opcao == "Gazelle":
    st.success("Você tem personalidade forte e bom gosto.")
elif opcao == "Forum":
    st.success("Você é moderno e confiante.")
elif opcao == "Superstar":
    st.success("Você gosta de se destacar.")
elif opcao == "NMD":
    st.success("Você ama conforto e inovação.")
elif opcao == "Ultraboost":
    st.success("Você busca performance e excelência.")

