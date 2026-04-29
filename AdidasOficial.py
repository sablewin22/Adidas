
import streamlit as st

st.title("O QUE O SEU TÊNIS ADIDAS DIZ SOBRE VOCÊ?")

st.markdown("##### Descubra a personalidade de cada modelo e veja qual combina mais com você!")

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

st.markdown("---")
st.markdown("## DESCUBRA O SEU")

opcao = st.selectbox(
    "Escolha o que mais combina com a sua personalidade:",
    ["Clique e escolha","Sou clássico e estiloso.","Sou criativo, leve e casual.","Tenho personalidade forte e bom gosto.","Sou moderno e confiante.","Gosta de me destacar.","Amo conforto e inovação.",
"Busco performance e excelência."]
)

if opcao == "Clique e escolha":
    st.write()
elif opcao == "Sou clássico e estiloso.":
    st.success("Modelo Samba")
    st.image('https://product-images-cdn.liketoknow.it/EcmHp.l1RPi0s5uVQ5GK07Hke2aef.jJU8NQyq3Dxu8Wl8GjLsrigSvFvNm2mtPTngynWlyfs8U_lW0Rjqp4eziwUwq.EX.ZnYK0h3hLpW4FypBIWNi4IpaK3RNdRPfnCBwoJpYSFVw9I4YDcaYiKw--?v=2&auto=format&fm=webp&w=256&h=256&fit=crop&q=80')
elif opcao == "Sou criativo, leve e casual.":
    st.success("Modelo Campus")
    st.image('https://product-images-cdn.liketoknow.it/parVcsO8ZaXogSxjpk0zUYgj3B4vInVCprY3xQv6THOXBjjfb5AleRCUsOnkHZFnDRFM5Jff7j_YKsuTFB5CvHalkrnWMTAV15wUrCtiGJ.tDcNeDffXI_LCBw9RyxB8Pe9KrQH1J5SSiRhmIzj6bQ--?v=2&auto=format&fm=webp&w=256&h=256&fit=crop&q=80')
elif opcao == "Tenho personalidade forte e bom gosto.":
    st.success("Modelo Gazelle")
    st.image('https://product-images-cdn.liketoknow.it/bh4XRiHKv3V1hdJD3ySFmBuucAfHfotrAAsl_ZmeqseU_Q93Pm6XQsgsnzeyiWSudUlh7GCxhAFJrjAhPWWAQaTsZlFFlCFHCHIs6WK69kWZfZmOhPGcr01N8SOX1Plzv3s.I8zTqI6AQxKUEElB?v=2&auto=format&fm=webp&w=256&h=256&fit=crop&q=80')
elif opcao == "Sou moderno e confiante.":
    st.success("Modelo Forum")
    st.image('https://images.tcdn.com.br/img/img_prod/873473/90_tenis_adidas_forum_low_cl_1591_1_edfd32f9a00012bc50fd162dcb13d716.png')
elif opcao == "Gosta de me destacar.":
    st.success("Modelo Superstar")
    st.image('https://product-images-cdn.liketoknow.it/TxvyEJp2xzT3tDdogSPGYz5efCX7aBwFSGdHhpKe9jPcuqfb.fAnUQ4H3QEAyx6e114gNJ81PmilTob4x9oD44Uzq9mjvS8Sak.fb3ztFU72p4g_tkL8sciCDLuT4iYnTcRA9w41eJuPW4vPCeJFXg--?v=2&auto=format&fm=webp&w=256&h=256&fit=crop&q=80')
elif opcao == "Amo conforto e inovação.":
    st.success("Modelo NMD")
    st.image('https://product-images-cdn.liketoknow.it/tBcdr6ybG4tfMcpwWkIHbugN5Cv4.GzVCk6XliYykMhUHCyVK2xf7VvRv_klQrvqB3BIZVqewOaQb6i6wFh9lcL8c2pOo57..2Hxe.EhnP9bfyfqiFGDXc1qxXYYfWBcUo8pI78YJdYYfcNLLRhvTw--?v=2&auto=format&fm=webp&w=256&h=256&fit=crop&q=80')
elif opcao == "Busco performance e excelência.":
    st.success("Modelo Ultraboost")
    st.image('https://cdn.shopify.com/s/files/1/0672/2106/1933/files/1103755_00_png.png?v=1739333100&width=256')

