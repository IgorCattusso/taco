-- Dishes
INSERT INTO taco.dishes ("uuid", "name") VALUES ('0c9be464-bf75-4a2b-8af8-f97d3747d580', 'Strogonoff de frango'),
('d269a78c-1ed1-448a-9b69-e3d8d3993dc9', 'Strogonoff de carne'),
('54a6fa05-48c9-46ac-8c3a-74a176428b26', 'Veggie stir fry'),
('5e6b9847-bcbb-409c-a7fe-211b16acf049', 'Chicken stir fry'),
('b422e671-10d0-4da0-bbee-a9ddafa6fe9e', 'Meat stir fry'),
('fec70a41-75ef-4754-9b4e-361fb16d4980', 'Guisado de vagem'),
('4fee8869-2d32-496b-adea-4c43380aeacd', 'Bifes de peito de frango'),
('a948c493-f5ed-4506-9614-b38c49645653', 'Feijoada'),
('7322766b-9773-4a14-aeee-638fca8874bf', 'Sopa de agnoline'),
('a4ad4c15-ca65-4263-b1ec-33a23ce394e4', 'Quiabo refogado'),
('e594f4d9-92a9-4340-9356-1341e84b9db3', 'Bife acebolado'),
('96c2c705-379e-4284-89a9-b2e0a701fb80', 'Pastel de frango'),
('7fd52e92-17f7-40e1-9727-391f553362b2', 'Pastel de carne'),
('10a2d205-e0fa-44a3-a447-4a36dd925dc6', 'Pastel de palmito e queijo'),
('1631a09c-138c-408c-8c2c-959e5c0e8f0f', 'Lasanha de frango'),
('d1003185-d3c7-41d7-8a5b-140654edb052', 'Lasanha de carne'),
('bf29e2f9-a28d-447b-8c69-ec7b7f08ae3f', 'Hambúrguer'),
('f11d925f-9d86-472f-8025-a8dd2fc9f1cf', 'Berinjela à milanesa'),
('e01d1aed-e0cd-4bcd-8b40-0b5ecfe156c2', 'Abobrinha à milanesa'),
('7edc3b43-40b8-4e70-9fd7-57ea58360f60', 'Bife bovino à milanesa'),
('9053ff19-6b76-4d26-829d-428df0baa4d0', 'Peito de frango à milanesa'),
('ede0d0dc-4ef8-4894-8667-0ec6bf614d84', 'Chicken nuggets'),
('65a56bdd-1dd0-422d-8805-bdb9e28239a7', 'Pizza com massa comprada'),
('e58b3ec0-47ea-44fa-865b-ca5b2f7ae01b', 'Pizza com massa feita'),
('3bb5c6ac-185b-4cc3-880e-e43f14ce8f86', 'Frango agridoce'),
('91b84572-a228-47ec-a085-3449cd74b039', 'Wraps de presunto e queijo'),
('96f83550-c4c9-41d1-ac01-18bb66de3b5b', 'Shawarma de frango'),
('5c03f2ce-edbb-4d18-bdcc-c469fa00a444', 'Shawarma de carne bovina'),
('ab2f19a7-0c67-4e41-a257-abcaa28b4e99', 'Honey chicken'),
('02e2d559-bbdc-4f5e-b3a7-77f880c589e5', 'Xis-sanduba'),
('1f09a6cd-21f0-4ece-87b2-adeb22571b12', 'Sanduíche baguette'),
('a90afa1b-673f-4f65-ac20-3604ab17fa71', 'Rolled pork belly'),
('1a883706-cb39-4855-8928-f19c863d51cc', 'Sobrecoxa de frango frita'),
('3a6a99a1-b46d-4727-9c03-2778763f6a52', 'Tábua de frios'),
('e9520cdf-0e3f-4d65-a94c-29a84590f5c7', 'Ragú'),
('7d0de96d-bda3-4837-98bd-22e87036a14b', 'Arroz branco'),
('cea34ebf-9852-4941-94da-f416959d9582', 'Frango cremoso com espinafre'),
('2b1fcca8-f5f8-42e1-b123-e7b70cf61b14', 'Panqueca de carne'),
('a81d398b-9098-46ed-ac07-bb3407441e7f', 'Nega maluca');

-- Ingredients
INSERT INTO taco.ingredients ("uuid", "name") VALUES ('546569b6-7538-43f9-bc3e-54384c25111d', 'Cebola amarela'),
('c95b8266-7a1c-44a9-8e37-902a64a6078b', 'Cebola roxa'),
('f2bbdb00-dac4-4da9-a450-912165a0d037', 'Dente de alho'),
('381939ec-69a9-4a06-8632-f159cddd9064', 'Sal'),
('db334add-4be1-48aa-b337-d75775f364a0', 'Azeite de oliva'),
('b3bf671a-4e7a-4c23-9061-2c26f92617c9', 'Óleo vegetal'),
('09f03e9b-d297-435f-8b64-7772b2e6cf18', 'Peito de frango'),
('49b8b153-e913-47bc-85d8-c7e68e900e37', 'Coxa de frango'),
('e37020af-7c5f-4ecf-a2ff-19bde0d7dd47', 'Sobrecoxa de frango'),
('fb160485-1493-4d2a-abe8-10d93b11bd1f', 'Carne moída de frango'),
('e7deb826-ce48-4640-9668-f4663d5e89da', 'Patinho bovino'),
('9a53f271-d796-48d3-905a-983b20ccb92c', 'Paleta bovina'),
('90c51815-d2da-43c3-a67b-6261e83d2818', 'Coxão mole bovino (de dentro)'),
('b623385b-251f-4495-9ab5-d7c49effdd72', 'Coxão duro bovino (de fora)'),
('5b3a9eeb-93f5-45d2-a3f9-55af5a2fb0f8', 'Peito bovino'),
('8498a083-46bb-4079-bf9f-6833bad6839e', 'Agulha bovina'),
('1a07aa7c-40b1-4075-8f2c-29727f2eb055', 'Carne moída bovina'),
('6b79ecdc-69d9-4c97-a496-e5598db2467a', 'Filé Mignon bovino'),
('96bdf892-1028-40f2-b781-a18dff265a83', 'Filé Mignon suíno'),
('88fae06c-02eb-4c54-9525-c1e89e8816a4', 'Bisteca suína'),
('c1744000-c6f1-4250-aa8a-7a6bf9a8a773', 'Pernil suíno'),
('d7d0419e-cea7-478e-8887-5685dfb3338e', 'Carré suíno'),
('f7fc1a86-5e90-4611-a28f-b4c694b02703', 'Carne moída suína'),
('a56410a1-47d3-47d7-8b4a-3dd7edb6e90f', 'Pimenta do reino'),
('ed6bb984-347e-4440-aafe-01293067e3c3', 'Açúcar cristal'),
('6fec984e-9416-445b-b5eb-326775aeba91', 'Açúcar mascavo'),
('b4f675cb-244b-4e3f-ab0e-3bb4364cc582', 'Mel'),
('081a0bcb-7ca1-4983-b183-704a899eec4a', 'Pimenta dedo de moça'),
('dd1dfc6a-be69-4258-a329-5e03df17ec7d', 'Pimenta cambuci'),
('8ce32972-3336-473d-8555-2927c13973dd', 'Adobo'),
('c2526f23-b52d-41da-8e7a-3762f2bb35b1', 'Pimenta da jamaica'),
('60baa111-4057-409e-a189-00f2fa0c40ea', 'Chimichurri'),
('877bcbd7-2ef2-424a-965a-0dfe1621be1c', 'Massa espaguete'),
('9ff7f94a-91b8-4e5f-8d89-f7561a4b60b8', 'Massa parafuso'),
('539a870d-9edd-4ab6-b4dc-4558cecb78b3', 'Massa para lasanha (fresca)'),
('2452e602-ab43-4aa3-81b2-40084e9b48c2', 'Massa para pastel'),
('b83773d6-599c-4a3e-bd1f-b8442fe38819', 'Milho enlatado'),
('abfedb9d-57e7-4261-b4ae-fb055e635ca7', 'Ervilha'),
('e33ccb8b-2305-4cbb-b3c3-823a3142aacd', 'Tomate italiano'),
('01eaabb4-cbeb-4f56-906c-934ddc72fdba', 'Tomate normal'),
('31b9d520-3c02-41cc-9cc6-8f3da18cd894', 'Tomate enlatado'),
('6a2dc754-9df0-4162-af06-8ca6b7c76fd2', 'Molho de tomate pronto'),
('4367f102-7b47-4aa9-bf73-d4d57916a41f', 'Orégano'),
('24be0a40-c3ea-4627-8672-5545f02c2335', 'Manjericão'),
('a2777088-b667-4b1a-902f-ac27a4f337de', 'Manjerona'),
('90aff2f5-7dc7-44b1-828b-84d3381d06b9', 'Sálvia'),
('0efa891e-1d61-4483-bf42-34af34dd90b3', 'Alecrim'),
('90f00d7c-e587-4fff-b835-ffa5402c85d5', 'Tomilho'),
('7a54a458-2e6a-4cc3-8858-c658348a381e', 'Extrato de tomate'),
('dd4fda4d-58a8-4d38-b987-b57cf47ef1c9', 'Nata'),
('3d1fdade-96e3-4340-891e-179a95a535a7', 'Creme de leite'),
('b2553c76-d523-4959-96cc-7e97621a9495', 'Batata inglesa'),
('f1c14d8d-402e-4522-80ba-a60da0e93312', 'Batata doce'),
('1843ddde-884d-49c1-a330-a388259257af', 'Farinha de trigo'),
('f1288561-0df6-49a9-be8c-19d52ce0c53f', 'Farinha de milho'),
('cb72dc49-bfd7-4c34-9a7a-3fcb1923a0c8', 'Água'),
('6a058171-924d-4271-acb0-5143b6839cb1', 'Farinha panko'),
('cd57fb44-7c1d-4833-aac3-52fd95235b7e', 'Ovo'),
('ddd6d6e9-c615-4324-b075-07b7e2d94f71', 'Fermento biológico'),
('4ce32c76-dde1-444f-9692-b643effbe57a', 'Manteiga com sal'),
('b931a1bc-e772-426e-abf4-1aa0e8ebf55e', 'Manteiga sem sal'),
('cd549b5e-ed76-43eb-ab56-ad553fa394cb', 'Fermento químico'),
('44954e8f-201e-4b43-802e-8ed63071189e', 'Amido de milho'),
('1c505609-c61a-4e26-8d65-76ad9ff69a25', 'Molho shoyu light'),
('edc1f5b6-f4fa-482a-8110-e6ef93ea8113', 'Molho de ostra'),
('1a9f2433-35f6-48e3-a8d8-5e116c86e4e4', 'Mirin'),
('21953068-eda0-4ac9-a445-ad64b7ad39f0', 'Vinho tinto'),
('7fa97511-a685-4d58-b893-5c0672348305', 'Vinho branco'),
('99faf6d3-ef9f-424e-8153-1ea545c1fa5a', 'Cogumelo paris'),
('6efe5fec-184c-44cb-a759-73f57be9dd28', 'Cogumelo portobello'),
('5a0acc7f-3267-47d1-9122-f762e1cb265a', 'Queijo mussarela'),
('51b0873c-87e6-4b13-8323-146c35ec9452', 'Presunto'),
('def1fb84-5a99-483e-981a-917ceb286a88', 'Queijo provolone'),
('339f8439-b8ea-46f4-bd52-456e27cfe303', 'Queijo brie'),
('6f7b52cc-28b3-4072-8638-9d62fc20501f', 'Alface'),
('160f53f2-b795-466a-89b6-ad2fce8a2aca', 'Beterraba'),
('8282b0b1-ee2e-4781-a3bf-fd4fbb58e2c7', 'Chuchu'),
('51221320-f952-4fa2-ae52-feeb9cda59d1', 'Pepino salada'),
('c99f4f1a-4952-459f-99c0-b0eec2106083', 'Pepino japonês'),
('fd8a197e-7c92-4f6d-b3d9-b3323ced29f0', 'Azeitona em conserva'),
('f9e906db-e745-4066-aadf-aefad58eb9b3', 'Pepino em conserva'),
('5cb8ff20-6f88-4384-a2a7-98207eae7149', 'Palmito em conserva'),
('aca1d139-984b-4646-8ee4-be0f7bd4926f', 'Couve folha'),
('371793db-c57f-4317-91a5-0c5ccfc79851', 'Couve chinesa'),
('da603fbd-dae1-4c7b-ba51-8dd1a5fd4ac1', 'Alho poró'),
('585bc72c-5b22-43a4-a724-1b718e099d21', 'Aipo'),
('f634e871-8703-45e2-8012-a4d1db54e33d', 'Salsa'),
('97b764c8-6e1d-473c-9792-029350f65d8e', 'Cebolinha'),
('669d166d-bf89-4545-bdd9-d7d44194a373', 'Espinafre'),
('a1acffd6-77d3-4aad-b41e-3140ecb3d4cf', 'Tomate seco'),
('10ea0129-194d-4fa6-b922-13a90937ed9c', 'MSG'),
('74aca605-047e-4592-ae43-613e98b34b1e', 'Sriracha'),
('383ed1e1-bd60-41b4-89d4-d02150ef649e', 'Caldo knorr de frango'),
('139a31c5-6add-4b95-9750-2adab4893916', 'Caldo knorr de carne'),
('eaf24f4e-b56d-46e6-87d0-86a8c3a86fb8', 'Caldo knorr de legumes'),
('e87cf616-3e5f-4761-abcd-3a4e6fc7a14c', 'Clara de ovo'),
('afb4eead-55b9-4399-83fa-f6b5d9560aae', 'Gema de ovo'),
('0d542521-96f1-4fa5-8448-1d1f2b4ecc55', 'Vinagre de arroz'),
('858d9255-51ec-4cc2-9f4a-10255d3d692e', 'Gergelim branco'),
('9322efeb-3ddd-434a-a356-2338116ee397', 'Gergelim preto'),
('829e2b59-f347-4de6-95d3-0a8174e5c518', 'Páprica doce'),
('c5155b94-dc09-4e1f-8b1f-77da4dcc5e46', 'Achocolatado em pó'),
('ea50b2dd-5046-4ec7-afdb-79e70af7eae0', 'Cacau em pó');

-- Measurement Units
INSERT INTO taco.measurement_units ("uuid", "name", "abbreviation") VALUES ('b027cdd4-5955-4389-903c-cdc4b90326d2', 'Grama', 'g'),
('bc790145-225d-4de7-8772-7028db145ef0', 'Mililitro', 'ml'),
('49f7eecc-6544-403a-811b-0a6a0f5266a7', 'Unidade', 'un');

-- Nutritional Values
INSERT INTO taco.nutritional_values ("uuid", "ingredient_uuid", "measurement_unit_uuid", "calories", "fats", "carbohydrates", "proteins", "sodium", "fiber") VALUES ('e4afd89a-f0b4-41ed-aeb2-863d9b9703e6', '546569b6-7538-43f9-bc3e-54384c25111d', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.42', '0.0008', '0.1011', '0.0092', '0.00003', '0.014'),
('821a3350-29f1-4077-89bb-cd82c9f7db0c', '546569b6-7538-43f9-bc3e-54384c25111d', '49f7eecc-6544-403a-811b-0a6a0f5266a7', '0.84', '0.0016', '0.2022', '0.0184', '0.00006', '0.028'),
('3bc223af-04a3-4050-898c-cd7c2e255562', 'c95b8266-7a1c-44a9-8e37-902a64a6078b', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.42', '0.0008', '0.1011', '0.0092', '0.00003', '0.014'),
('224d1cd0-7227-40fb-8ea2-08cd44ca4ab6', 'f2bbdb00-dac4-4da9-a450-912165a0d037', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.49', '0.005', '0.3306', '0.0636', '0.00017', '0.021'),
('bbf11e37-bf6c-47db-ba15-a90f23244d8d', 'f2bbdb00-dac4-4da9-a450-912165a0d037', '49f7eecc-6544-403a-811b-0a6a0f5266a7', '5.96', '0.02', '1.3224', '0.2544', '0.00068', '0.084'),
('5d93e9d4-bd16-4bc9-87d1-f24799b6619f', '381939ec-69a9-4a06-8632-f159cddd9064', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0', '0', '0', '0', '0.38758', '0'),
('8aacb571-34cd-4406-a25b-f91909ecd1ff', 'db334add-4be1-48aa-b337-d75775f364a0', 'bc790145-225d-4de7-8772-7028db145ef0', '9.82124', '1.111', '0', '0', '0.00002', '0'),
('bec70501-53bd-49a8-bc48-c184c43cafd1', 'b3bf671a-4e7a-4c23-9061-2c26f92617c9', 'bc790145-225d-4de7-8772-7028db145ef0', '9.60908', '1.087', '0', '0', '0', '0'),
('3cb333a1-dd65-4e37-ab61-c3f7d8b598cf', '09f03e9b-d297-435f-8b64-7772b2e6cf18', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.95', '0.0772', '0', '0.2955', '0.00393', '0'),
('df98e75c-d4af-458f-9f42-8a4c16ad05d5', '49b8b153-e913-47bc-85d8-c7e68e900e37', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.14', '0.1106', '0', '0.268', '0.00412', '0'),
('4ef25db1-6fac-467d-87c8-07faaabe0f19', 'e37020af-7c5f-4ecf-a2ff-19bde0d7dd47', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.45', '0.1536', '0', '0.2485', '0.00406', '0'),
('e19bde7d-ac09-4442-805c-a8ad1284987c', 'fb160485-1493-4d2a-abe8-10d93b11bd1f', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.37', '0.1349', '0', '0.2707', '0.00404', '0'),
('4a22cd9d-4f8e-4b9c-833c-0f70c93b6d10', 'e7deb826-ce48-4640-9668-f4663d5e89da', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.27', '0.0243', '0', '0.2455', '0.00061', '0'),
('e4c74eff-159b-44bb-a176-ffa19f050f6b', '9a53f271-d796-48d3-905a-983b20ccb92c', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.29', '0.0541', '0', '0.1884', '0.00058', '0'),
('53923282-5b3b-432b-ba1b-bd0838a342f9', '90c51815-d2da-43c3-a67b-6261e83d2818', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.69', '0.087', '0', '0.212', '0.00061', '0'),
('e904fdf0-30a4-499a-bc00-c011a5f8f693', 'b623385b-251f-4495-9ab5-d7c49effdd72', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.21', '0.043', '0', '0.21', '0.00071', '0'),
('223bebdc-37ab-4666-b8c2-fc1cff57c201', '5b3a9eeb-93f5-45d2-a3f9-55af5a2fb0f8', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.55', '0.07', '0', '0.21', '0.00062', '0'),
('1a0d7323-7806-4ced-a61b-b12409c2e610', '8498a083-46bb-4079-bf9f-6833bad6839e', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.04', '0.1314', '0', '0.2007', '0.00064', '0'),
('08ba21fc-a49c-42e8-926f-65e0a78e953b', '1a07aa7c-40b1-4075-8f2c-29727f2eb055', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.69', '0.1767', '0', '0.2554', '0.00087', '0'),
('5d4daea4-ae26-468a-b9f7-b9673892f155', '6b79ecdc-69d9-4c97-a496-e5598db2467a', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.93', '0.119', '0', '0.2003', '0.00043', '0'),
('3ecb0d9a-626a-4341-9820-0d84524aaaf1', '96bdf892-1028-40f2-b781-a18dff265a83', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.06', '0.02', '0', '0.22', '0.0008', '0'),
('56422bd6-6ba2-4e24-9bb9-ce067fb6c283', '88fae06c-02eb-4c54-9525-c1e89e8816a4', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.46', '0.054', '0', '0.24', '0.00088', '0'),
('e1f400cd-c9e4-47ae-b6ac-147d427cb5f9', 'c1744000-c6f1-4250-aa8a-7a6bf9a8a773', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.7', '0.088', '0', '0.23', '0.0008', '0'),
('b06e8b22-41f4-48f5-b6f2-7fa901e80b40', 'd7d0419e-cea7-478e-8887-5685dfb3338e', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.42', '0.14', '0', '0.27', '0.00062', '0'),
('ddc20a43-aa65-4969-998b-c1fbbc36f3c0', 'f7fc1a86-5e90-4611-a28f-b4c694b02703', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.06', '0.14', '0', '0.2', '0.0008', '0'),
('c1a97591-1ec3-46f8-9932-35c50668a04e', 'a56410a1-47d3-47d7-8b4a-3dd7edb6e90f', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.55', '0.0326', '0.6481', '0.1095', '0.00044', '0.265'),
('38633776-0739-4766-8c7b-07fa9c66428e', 'ed6bb984-347e-4440-aafe-01293067e3c3', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.87', '0', '0.9998', '0', '0', '0'),
('ed969fa9-2d7a-4489-bc25-57a01c1a60d6', '6fec984e-9416-445b-b5eb-326775aeba91', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.77', '0', '0.9733', '0', '0.00039', '0'),
('bda8d1ab-ab04-4418-94e6-2622984293ce', 'b4f675cb-244b-4e3f-ab0e-3bb4364cc582', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.04', '0', '0.824', '0.003', '0.00004', '0.002'),
('96ace3d3-2da5-4af2-9c1e-8f20af34962b', 'b4f675cb-244b-4e3f-ab0e-3bb4364cc582', 'bc790145-225d-4de7-8772-7028db145ef0', '2.14016', '0', '0.580096', '0.002112', '0.00002816', '0.001408'),
('a95a9be8-94c7-496a-8667-8a49df8d3cda', '081a0bcb-7ca1-4983-b183-704a899eec4a', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.27', '0.0045', '0.0535', '0.0166', '0.00013', '0.034'),
('446fb047-f023-4834-85fd-352bce3885a9', 'dd1dfc6a-be69-4258-a329-5e03df17ec7d', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.4', '0.0025', '0.0971', '0.0118', '0.00002', '0.031'),
('2a6990cd-c27f-4edf-930a-08e48643eb0d', '8ce32972-3336-473d-8555-2927c13973dd', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0', '0', '0', '0', '0', '0'),
('c80604c6-7223-4ca6-8d84-79a05ebf4941', 'c2526f23-b52d-41da-8e7a-3762f2bb35b1', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.23', '0.003', '0.051', '0.011', '0.00014', '0.019'),
('98c49975-38fe-4beb-bf9b-310b67b40dcf', '60baa111-4057-409e-a189-00f2fa0c40ea', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0', '0', '0', '0', '0', '0'),
('a9d09ef7-fd0b-4c48-9780-1ff946eb3c50', '877bcbd7-2ef2-424a-965a-0dfe1621be1c', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.36', '0.008', '0.27', '0.047', '0', '0.008'),
('170e9587-09d0-4260-88f1-188fce7205c5', '9ff7f94a-91b8-4e5f-8d89-f7561a4b60b8', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.21', '0.007', '0.24', '0.041', '0', '0.016'),
('87564bd7-ad46-495f-a79c-76d4ed90d72d', '539a870d-9edd-4ab6-b4dc-4558cecb78b3', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.6', '0.027', '0.49', '0.099', '0.00167', '0'),
('d1329808-6adc-436f-8b01-1efe238bb9f2', '2452e602-ab43-4aa3-81b2-40084e9b48c2', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.7', '0.03', '0.54', '0.07', '0.00603', '0.002'),
('f9d2b3f4-826e-439a-a7fd-e6aa841e4038', 'b83773d6-599c-4a3e-bd1f-b8442fe38819', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.59', '0.017', '0.078', '0.03', '0.0023', '0.034'),
('367ad6f2-12b9-407c-a207-b03a6c8a7f2b', 'abfedb9d-57e7-4261-b4ae-fb055e635ca7', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.77', '0.0037', '0.1371', '0.0521', '0.00112', '0.042'),
('487baf74-0a3a-4253-9760-4460cbc8bbf6', 'e33ccb8b-2305-4cbb-b3c3-823a3142aacd', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.18', '0.002', '0.0392', '0.0088', '0.00005', '0.012'),
('581891a8-856d-456b-8843-0bf020fcc3c9', '01eaabb4-cbeb-4f56-906c-934ddc72fdba', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.18', '0.002', '0.0392', '0.0088', '0.00005', '0.012'),
('fe9ad4e6-9b75-4988-8bc4-8f281d5f0b6a', '31b9d520-3c02-41cc-9cc6-8f3da18cd894', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.17', '0.0013', '0.0391', '0.0008', '0.00128', '0.009'),
('81654c1e-242f-4288-86ca-f36e93bf8b23', '31b9d520-3c02-41cc-9cc6-8f3da18cd894', '49f7eecc-6544-403a-811b-0a6a0f5266a7', '6.8', '0.052', '1.564', '0.032', '0.0512', '0.36'),
('31ac2189-891c-42ea-9b0d-8f5b3856c3c2', '6a2dc754-9df0-4162-af06-8ca6b7c76fd2', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.53', '0', '0.115', '0.01', '0.00535', '0.0117'),
('c65a83c5-199e-4626-990e-1dfec72eac1e', '4367f102-7b47-4aa9-bf73-d4d57916a41f', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0', '0', '0', '0', '0', '0'),
('b92ef5fc-5770-4bbd-8ef4-931afb614a86', '24be0a40-c3ea-4627-8672-5545f02c2335', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0', '0', '0', '0', '0', '0'),
('1aca8173-a3f3-4685-a598-6b0514c78d49', 'a2777088-b667-4b1a-902f-ac27a4f337de', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0', '0', '0', '0', '0', '0'),
('8ced37f0-a46d-4e87-97bc-60de3ffd8f6a', '90aff2f5-7dc7-44b1-828b-84d3381d06b9', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0', '0', '0', '0', '0', '0'),
('1bee9cd1-bd4b-488b-bf26-a45fec131132', '0efa891e-1d61-4483-bf42-34af34dd90b3', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0', '0', '0', '0', '0', '0'),
('a8a7d038-0c5f-4a5c-aece-ad2d4d1153df', '90f00d7c-e587-4fff-b835-ffa5402c85d5', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0', '0', '0', '0', '0', '0'),
('13b60009-f4f7-46aa-ae27-98c0d57c5624', '7a54a458-2e6a-4cc3-8858-c658348a381e', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.37', '0', '0.07', '0.02', '0.00383', '0.033'),
('2bc3e69f-e088-418a-8bc6-67faf6aa1a18', 'dd4fda4d-58a8-4d38-b987-b57cf47ef1c9', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '4.32', '0.48', '0', '0', '0.00036', '0'),
('74a54ba2-debd-47a2-8833-18ece67af3ea', '3d1fdade-96e3-4340-891e-179a95a535a7', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.95', '0.1931', '0.0366', '0.027', '0.0004', '0'),
('646e3756-5a15-4327-a409-5da74583a593', '3d1fdade-96e3-4340-891e-179a95a535a7', '49f7eecc-6544-403a-811b-0a6a0f5266a7', '390', '38.62', '7.32', '5.4', '0.08', '0'),
('55aff9b4-15bc-4c8f-9b66-9117661e6119', 'b2553c76-d523-4959-96cc-7e97621a9495', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.82', '0.0012', '0.19', '0.02', '0.00007', '0.021'),
('2a7268e5-ef2c-42c7-893b-3d58184aac64', 'f1c14d8d-402e-4522-80ba-a60da0e93312', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.86', '0.0005', '0.2012', '0.0157', '0.00055', '0.03'),
('3f5fa084-5f08-4613-ac10-03417725865a', '1843ddde-884d-49c1-a330-a388259257af', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.64', '0.0098', '0.7631', '0.1033', '0.00002', '0.027'),
('e3ba5a7c-115b-4c52-95be-32b84f5d6814', 'f1288561-0df6-49a9-be8c-19d52ce0c53f', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.58', '0.012', '0.8', '0.07', '0.00009', '0.018'),
('d062f3ca-2ed3-40c5-b234-e552c727b121', 'cb72dc49-bfd7-4c34-9a7a-3fcb1923a0c8', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0', '0', '0', '0', '0', '0'),
('fca1b3cf-4263-4660-b95c-097721795e2c', 'cb72dc49-bfd7-4c34-9a7a-3fcb1923a0c8', 'bc790145-225d-4de7-8772-7028db145ef0', '0', '0', '0', '0', '0', '0'),
('469e6a13-8ef3-470b-82f8-492d02d4af7c', '6a058171-924d-4271-acb0-5143b6839cb1', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.73', '0', '0.8', '0.1', '0.00433', '0.0333'),
('c23d2e13-1914-4740-b010-d9d573bb63c7', 'cd57fb44-7c1d-4833-aac3-52fd95235b7e', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.47', '0.0994', '0.0077', '0.1258', '0.0014', '0'),
('f7bc28bf-3fe6-4b39-8577-e53cad38d812', 'ddd6d6e9-c615-4324-b075-07b7e2d94f71', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.04', '0.056', '0.22', '0.41', '0.0013', '0.2'),
('0802b6c1-b040-402b-977f-21d2383a9044', '4ce32c76-dde1-444f-9692-b643effbe57a', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '7.4', '0.82', '0', '0', '0.0074', '0'),
('2faf05a5-2c16-49b4-94e1-ccead4be9184', 'b931a1bc-e772-426e-abf4-1aa0e8ebf55e', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '7.4', '0.82', '0', '0', '0.001', '0'),
('6eb6a16d-1e42-471e-859e-bb9367df937d', 'cd549b5e-ed76-43eb-ab56-ad553fa394cb', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.2', '0', '0.094', '0.001', '0.0001', '0'),
('651f0467-b665-49aa-bc58-0d76e409c986', '44954e8f-201e-4b43-802e-8ed63071189e', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.5', '0', '0.85', '0', '0', '0'),
('4fc40100-c7e6-4a57-91bc-91d829735197', '1c505609-c61a-4e26-8d65-76ad9ff69a25', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.36', '0', '0.036', '0.048', '0.04992', '0.012'),
('fbdb221e-9cdf-4409-a2b3-e9ad1d08ee29', '1c505609-c61a-4e26-8d65-76ad9ff69a25', 'bc790145-225d-4de7-8772-7028db145ef0', '0.3', '0', '0.03', '0.04', '0.0416', '0.01'),
('a75c97b8-2a85-4748-8c46-6f06646532d4', 'edc1f5b6-f4fa-482a-8110-e6ef93ea8113', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.51', '0.0025', '0.1092', '0.0135', '0.02733', '0.003'),
('05fea00d-4428-4c73-aac4-ce1bb787933c', 'edc1f5b6-f4fa-482a-8110-e6ef93ea8113', 'bc790145-225d-4de7-8772-7028db145ef0', '0.419063270336894', '0.00205423171733772', '0.0897288414133114', '0.0110928512736237', '0.0224568611339359', '0.00246507806080526'),
('60b307d3-7d03-47e6-b3c3-fc68a2da03ce', '1a9f2433-35f6-48e3-a8d8-5e116c86e4e4', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.87', '0', '0.71', '0', '0', '0'),
('04f3c72e-efdf-4aa7-8a18-987ca28061b8', '1a9f2433-35f6-48e3-a8d8-5e116c86e4e4', 'bc790145-225d-4de7-8772-7028db145ef0', '2.87', '0', '0.71', '0', '0', '0'),
('bea5c8d0-9ebe-42b0-a6b5-f174da069431', '21953068-eda0-4ac9-a445-ad64b7ad39f0', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.84', '0', '0.026', '0.0007', '0', '0'),
('b6b28458-9674-4c6a-a46d-f89ebbd1e54f', '21953068-eda0-4ac9-a445-ad64b7ad39f0', 'bc790145-225d-4de7-8772-7028db145ef0', '0.84168', '0', '0.026052', '0.0007014', '0', '0'),
('d2e8b9aa-9e6a-45a1-a08e-2d7d3c2adec6', '7fa97511-a685-4d58-b893-5c0672348305', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.81', '0', '0.0203', '0.0007', '0', '0'),
('adfd6945-7582-45e1-bf14-26c12fdc951b', '7fa97511-a685-4d58-b893-5c0672348305', 'bc790145-225d-4de7-8772-7028db145ef0', '0.81162', '0', '0.0203406', '0.0007014', '0', '0'),
('5bca841c-f572-4512-aa11-38fce6398a35', '99faf6d3-ef9f-424e-8153-1ea545c1fa5a', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.23', '0.0064', '0.0343', '0.031', '0.00006', '0.02'),
('dae68076-6d66-4adc-bb8a-02222527aaf0', '6efe5fec-184c-44cb-a759-73f57be9dd28', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.26', '0.002', '0.0507', '0.025', '0.00006', '0.015'),
('25b4c4a6-24ec-4792-b2c9-b5bfb138f5be', '5a0acc7f-3267-47d1-9122-f762e1cb265a', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.02', '0.2003', '0.0383', '0.2596', '0.00528', '0'),
('b1e05dbb-9a1b-4649-b7bd-d7da6940406a', '51b0873c-87e6-4b13-8323-146c35ec9452', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.85', '0.015', '0.01', '0.1675', '0.01115', '0'),
('bcf6505c-2192-4d91-96fa-0dceb4d89715', 'def1fb84-5a99-483e-981a-917ceb286a88', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.51', '0.2665', '0.0214', '0.2558', '0.00876', '0'),
('5632a6d4-011b-4cbb-a9de-9ae5c6ff734b', '339f8439-b8ea-46f4-bd52-456e27cfe303', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.34', '0.2768', '0.0045', '0.2075', '0.00629', '0'),
('1ee522f4-5b76-4583-b7b6-206d8ff69fd8', '6f7b52cc-28b3-4072-8638-9d62fc20501f', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.14', '0.0014', '0.0297', '0.009', '0.0001', '0.012'),
('d0bda2ee-69e3-4a92-a647-e507e23cb395', '160f53f2-b795-466a-89b6-ad2fce8a2aca', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.43', '0.0017', '0.0956', '0.0161', '0.00078', '0.028'),
('f7829b6c-3b89-4b83-baa1-959e7ba07bbe', '8282b0b1-ee2e-4781-a3bf-fd4fbb58e2c7', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.17', '0.0013', '0.039', '0.0082', '0.00002', '0.017'),
('f449a901-cd0f-4151-a164-1e4b51655646', '51221320-f952-4fa2-ae52-feeb9cda59d1', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.15', '0.0011', '0.0363', '0.0065', '0.00002', '0.005'),
('0cbf04cb-a843-4117-9aa5-c46e83da2cde', 'c99f4f1a-4952-459f-99c0-b0eec2106083', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.13', '0.0014', '0.0268', '0.0071', '0.00007', '0.006'),
('c56052d4-de6d-431e-ae5c-accebbb736d4', 'fd8a197e-7c92-4f6d-b3d9-b3323ced29f0', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.45', '0.15', '0', '0', '0.01385', '0.035'),
('b15d5727-f393-43dd-b669-7be80d89d8fd', 'f9e906db-e745-4066-aadf-aefad58eb9b3', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.34', '0', '0.076', '0.008', '0.0054', '0.008'),
('a0378b70-2663-4b06-abcc-2b304012349e', '5cb8ff20-6f88-4384-a2a7-98207eae7149', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.28', '0', '0.034', '0.024', '0.00308', '0.032'),
('0fcadef5-677c-4a8c-9b7a-ef05d1f15ecc', 'aca1d139-984b-4646-8ee4-be0f7bd4926f', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.27', '0.0039', '0.0489', '0.0266', '0.00015', '0.027'),
('76680920-940a-420d-b1f0-47c0dbf94817', '371793db-c57f-4317-91a5-0c5ccfc79851', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.15', '0.002', '0.0278', '0.0147', '0.00033', '0.011'),
('6a877cb1-03ea-4fe1-b9cc-82d32041d1a4', 'da603fbd-dae1-4c7b-ba51-8dd1a5fd4ac1', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.61', '0.003', '0.1415', '0.015', '0.0002', '0.018'),
('168ab139-a5ad-4e5d-9bd6-2be374ecb1dd', '585bc72c-5b22-43a4-a724-1b718e099d21', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.14', '0.0017', '0.0297', '0.0069', '0.0008', '0.016'),
('8427af41-a4eb-48d3-8277-039e82021ad2', 'f634e871-8703-45e2-8012-a4d1db54e33d', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.23', '0.0052', '0.0367', '0.0213', '0.00046', '0.028'),
('e57e1ccd-9b1b-41e2-9c3d-828eb6b7a036', '97b764c8-6e1d-473c-9792-029350f65d8e', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.25', '0.001', '0.0565', '0.018', '0.00004', '0.035'),
('21ab23c0-e927-4f5b-9698-d4c3177b618c', '669d166d-bf89-4545-bdd9-d7d44194a373', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.23', '0.0039', '0.0363', '0.0286', '0.00079', '0.022'),
('92f02985-2492-412a-8397-ab4d3cc08abd', 'a1acffd6-77d3-4aad-b41e-3140ecb3d4cf', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.225', '0.2325', '0.2325', '0.05', '0.00355', '0.0375'),
('f5968565-cdcf-4512-b00a-2140215eb5d2', '10ea0129-194d-4fa6-b922-13a90937ed9c', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1', '0', '1', '0', '0.128', '0'),
('26fc42e7-2133-4899-8a64-bb9b766ea523', '74aca605-047e-4592-ae43-613e98b34b1e', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '1.01', '0.0024', '0.25', '0.011', '0.01709', '0.009'),
('e7a82cb3-2375-418a-b2f8-75aea62f57ff', '383ed1e1-bd60-41b4-89d4-d02150ef649e', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '5.25', '0.325', '0.6', '0', '0', '0'),
('958471b8-906c-452d-8d06-f19b57374ba1', '383ed1e1-bd60-41b4-89d4-d02150ef649e', '49f7eecc-6544-403a-811b-0a6a0f5266a7', '21', '1.3', '2.4', '0', '0', '0'),
('03bc163b-fca6-4067-a41a-cb9dbb73b63d', '139a31c5-6add-4b95-9750-2adab4893916', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '5.25', '0.325', '0.6', '0', '0', '0'),
('adb1739a-a91c-4565-b6ea-25a4a1be3acf', '139a31c5-6add-4b95-9750-2adab4893916', '49f7eecc-6544-403a-811b-0a6a0f5266a7', '21', '1.3', '2.4', '0', '0', '0'),
('e35f2676-c4f6-4d89-b076-7d3ec0f6e8fc', 'eaf24f4e-b56d-46e6-87d0-86a8c3a86fb8', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '5.25', '0.325', '0.6', '0', '0', '0'),
('7556c75b-8389-44f5-b620-46c0179c25dc', 'eaf24f4e-b56d-46e6-87d0-86a8c3a86fb8', '49f7eecc-6544-403a-811b-0a6a0f5266a7', '21', '1.3', '2.4', '0', '0', '0'),
('0a51438f-08a6-4cfc-bf9e-c3dc3b220e11', 'e87cf616-3e5f-4761-abcd-3a4e6fc7a14c', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.52', '0.0017', '0.0073', '0.109', '0.00166', '0'),
('aa122597-8ed9-4a97-9aeb-7e26657cdefa', 'e87cf616-3e5f-4761-abcd-3a4e6fc7a14c', '49f7eecc-6544-403a-811b-0a6a0f5266a7', '15.6', '0.051', '0.219', '3.27', '0.0498', '0'),
('da5ceb31-d263-435c-8b53-e5f62ddf14a1', 'afb4eead-55b9-4399-83fa-f6b5d9560aae', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '3.22', '0.2654', '0.0359', '0.1586', '0.00048', '0'),
('d8d33234-1c57-4904-be24-1f744eadd529', '0d542521-96f1-4fa5-8448-1d1f2b4ecc55', 'bc790145-225d-4de7-8772-7028db145ef0', '0.178962020282362', '0', '0.00039769337840525', '0', '0.0000198846689202625', '0'),
('a22cf71e-1ec8-4589-92d6-4edb2336ec70', '0d542521-96f1-4fa5-8448-1d1f2b4ecc55', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '0.18', '0', '0.0004', '0', '0.00002', '0'),
('6cf66d67-1e9d-44a5-8e7b-e7f1afaccf4c', '858d9255-51ec-4cc2-9f4a-10255d3d692e', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '5.73', '0.4967', '0.2345', '0.1773', '0.00011', '0.118'),
('7f5a070e-95e0-4720-8789-7d8b384dc46b', '829e2b59-f347-4de6-95d3-0a8174e5c518', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.89', '0.1295', '0.5574', '0.1476', '0.00034', '0.374'),
('6033ffc7-948a-4528-9572-116614fa9a88', 'ea50b2dd-5046-4ec7-afdb-79e70af7eae0', 'b027cdd4-5955-4389-903c-cdc4b90326d2', '2.29', '0.137', '0.543', '0.196', '0.00021', '0.332');

-- Recipes
INSERT INTO taco.recipes ("uuid", "dish_uuid", "nutritional_value_uuid", "amount") VALUES ('65220166-77fc-46a9-99c2-61baf972618e', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', '821a3350-29f1-4077-89bb-cd82c9f7db0c', '1'),
('0df3b763-1a22-4f10-afa1-8a276f65b5d1', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', 'bbf11e37-bf6c-47db-ba15-a90f23244d8d', '3'),
('871626c0-5fa2-4a47-b922-b26785327e6e', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', '74a54ba2-debd-47a2-8833-18ece67af3ea', '150'),
('c206e7c6-1cf5-4945-86b0-3256c8b3fe81', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', '8427af41-a4eb-48d3-8277-039e82021ad2', '0'),
('143cc0aa-0845-4cfd-b96d-539da375fe88', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', 'e4c74eff-159b-44bb-a176-ffa19f050f6b', '300'),
('c62f2015-768e-405f-98bc-564873aec40c', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', '5d93e9d4-bd16-4bc9-87d1-f24799b6619f', '2'),
('1dcc5868-e866-4d60-9392-6fc1a2f8f942', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', '2a6990cd-c27f-4edf-930a-08e48643eb0d', '0'),
('df0106b8-9dc3-44ba-9ef1-eb0c14b00228', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', 'c1a97591-1ec3-46f8-9932-35c50668a04e', '0'),
('be7814f8-c7d2-4667-9506-2fbb2ce08748', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', 'a8a7d038-0c5f-4a5c-aece-ad2d4d1153df', '0'),
('95686ffa-c2ec-434c-a329-dc6e9c64f830', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', '5bca841c-f572-4512-aa11-38fce6398a35', '150'),
('8574e665-7840-4d51-8492-b35687e8ea81', 'd269a78c-1ed1-448a-9b69-e3d8d3993dc9', 'adb1739a-a91c-4565-b6ea-25a4a1be3acf', '1'),
('938845b5-2571-4642-84fb-3ddacaf41cce', '0c9be464-bf75-4a2b-8af8-f97d3747d580', '821a3350-29f1-4077-89bb-cd82c9f7db0c', '1'),
('f69ca7ba-d98b-489d-beb7-1989e01872e6', '0c9be464-bf75-4a2b-8af8-f97d3747d580', 'bbf11e37-bf6c-47db-ba15-a90f23244d8d', '3'),
('76d67bff-e0f5-46aa-b9a8-68707cf82d5c', '0c9be464-bf75-4a2b-8af8-f97d3747d580', '81654c1e-242f-4288-86ca-f36e93bf8b23', '3'),
('01c7ac49-043e-42b8-ae87-a2da3848aa4c', '0c9be464-bf75-4a2b-8af8-f97d3747d580', '646e3756-5a15-4327-a409-5da74583a593', '1'),
('f0615d84-7e7b-4765-b43e-d31ba0b30d24', '0c9be464-bf75-4a2b-8af8-f97d3747d580', '8427af41-a4eb-48d3-8277-039e82021ad2', '0'),
('06e74576-10fa-462d-a854-f3fd9515efe7', '0c9be464-bf75-4a2b-8af8-f97d3747d580', '3cb333a1-dd65-4e37-ab61-c3f7d8b598cf', '300'),
('e4cbb8e8-62b2-4f5a-ad1d-1850f611d260', '0c9be464-bf75-4a2b-8af8-f97d3747d580', '5d93e9d4-bd16-4bc9-87d1-f24799b6619f', '2'),
('dc0a5ffe-6e7a-43f9-a97f-17bfc02beba0', '0c9be464-bf75-4a2b-8af8-f97d3747d580', '2a6990cd-c27f-4edf-930a-08e48643eb0d', '0'),
('2c44212b-5b2c-45e9-b599-f7d04c92adca', '0c9be464-bf75-4a2b-8af8-f97d3747d580', 'c1a97591-1ec3-46f8-9932-35c50668a04e', '0'),
('e5d2fbed-a8ee-478a-a5a5-c69354d39588', '0c9be464-bf75-4a2b-8af8-f97d3747d580', '1aca8173-a3f3-4685-a598-6b0514c78d49', '0'),
('d754a8f5-82e6-49e0-a82b-c6b39451a4ff', '0c9be464-bf75-4a2b-8af8-f97d3747d580', 'dae68076-6d66-4adc-bb8a-02222527aaf0', '150'),
('05e9c91e-cbdf-4638-9871-d571c74c323d', '0c9be464-bf75-4a2b-8af8-f97d3747d580', '958471b8-906c-452d-8d06-f19b57374ba1', '1'),
('21a456c8-164a-4629-ba8e-7cd6d9e6a0c1', '0c9be464-bf75-4a2b-8af8-f97d3747d580', 'bec70501-53bd-49a8-bc48-c184c43cafd1', '100'),
('a807d88e-6fb1-4d9f-a095-540f00232c79', '0c9be464-bf75-4a2b-8af8-f97d3747d580', 'f5968565-cdcf-4512-b00a-2140215eb5d2', '2'),
('f46d6eaf-bf61-4c90-98f8-2184b2547214', 'cea34ebf-9852-4941-94da-f416959d9582', '821a3350-29f1-4077-89bb-cd82c9f7db0c', '1'),
('a02781c0-39cd-4657-ad6e-8aee8ec82365', 'cea34ebf-9852-4941-94da-f416959d9582', 'bbf11e37-bf6c-47db-ba15-a90f23244d8d', '3'),
('1d90d8d2-bb1f-45d8-b4b7-b8cedba647ca', 'cea34ebf-9852-4941-94da-f416959d9582', '2a6990cd-c27f-4edf-930a-08e48643eb0d', '0'),
('b7633b1b-6214-4cdf-b4b5-fc899f68bad5', 'cea34ebf-9852-4941-94da-f416959d9582', '81654c1e-242f-4288-86ca-f36e93bf8b23', '3'),
('d8f8a9fc-9292-4334-a445-476ce4fd8ad5', 'cea34ebf-9852-4941-94da-f416959d9582', '3cb333a1-dd65-4e37-ab61-c3f7d8b598cf', '300'),
('02c46759-86fc-45b1-8778-da88227f43f1', 'cea34ebf-9852-4941-94da-f416959d9582', '2bc3e69f-e088-418a-8bc6-67faf6aa1a18', '100'),
('1c8d4132-c5b0-4693-8407-374f58129e52', 'cea34ebf-9852-4941-94da-f416959d9582', '8427af41-a4eb-48d3-8277-039e82021ad2', '0'),
('c583b276-a2da-473b-ac79-f04e4d2e08f1', 'cea34ebf-9852-4941-94da-f416959d9582', '5d93e9d4-bd16-4bc9-87d1-f24799b6619f', '2'),
('3c6c8901-b2dc-4c93-83a5-4d51cc49565d', 'cea34ebf-9852-4941-94da-f416959d9582', 'f5968565-cdcf-4512-b00a-2140215eb5d2', '2'),
('9ec5f9aa-a380-464a-b474-ff2140c63913', 'cea34ebf-9852-4941-94da-f416959d9582', 'c1a97591-1ec3-46f8-9932-35c50668a04e', '0'),
('ee8d73df-98c9-4cc9-8b0c-caf6aaf9def6', 'cea34ebf-9852-4941-94da-f416959d9582', '958471b8-906c-452d-8d06-f19b57374ba1', '2'),
('e3526a1c-14c7-43cd-b93d-1ac4e2ae511a', 'cea34ebf-9852-4941-94da-f416959d9582', '21ab23c0-e927-4f5b-9698-d4c3177b618c', '300'),
('1cb664b6-0513-4ca3-9b32-580e208ad1a0', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', '3cb333a1-dd65-4e37-ab61-c3f7d8b598cf', '800'),
('3d5399b8-7eff-426e-96d8-252620364532', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', 'fbdb221e-9cdf-4409-a2b3-e9ad1d08ee29', '45'),
('93005a57-e20f-453c-baad-efdcf16577b6', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', '04f3c72e-efdf-4aa7-8a18-987ca28061b8', '30'),
('80a9c690-11c6-42c8-8b26-d73dc6445e73', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', 'c1a97591-1ec3-46f8-9932-35c50668a04e', '0'),
('6654177a-bf5e-4676-98f2-7c25eab6cd23', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', 'aa122597-8ed9-4a97-9aeb-7e26657cdefa', '1'),
('ee959f9e-c057-46e5-9dc9-56505d5a36ab', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', 'bbf11e37-bf6c-47db-ba15-a90f23244d8d', '5'),
('575abf48-f5de-405c-b9ad-b5d567697384', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', '5d93e9d4-bd16-4bc9-87d1-f24799b6619f', '4'),
('000b5156-44eb-4bed-9600-069d0e5f1931', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', 'f5968565-cdcf-4512-b00a-2140215eb5d2', '4'),
('b012620f-000e-41b4-a1a6-4c9728cc5185', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', '958471b8-906c-452d-8d06-f19b57374ba1', '1'),
('84c1736c-c0cd-4d55-8dea-944c6608a153', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', 'd8d33234-1c57-4904-be24-1f744eadd529', '15'),
('e9ca0c71-69a6-4a9b-8c12-a216d12e76ac', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', '96ace3d3-2da5-4af2-9c1e-8f20af34962b', '45'),
('d65512a6-fd0d-4d4f-91e4-7376bfa6f37a', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', '651f0467-b665-49aa-bc58-0d76e409c986', '150'),
('5760426c-9157-491e-a42a-d2f65fbb0580', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', '3f5fa084-5f08-4613-ac10-03417725865a', '150'),
('61f8034f-37b4-4cb5-ac6f-02f428865ceb', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', '6eb6a16d-1e42-471e-859e-bb9367df937d', '17'),
('fd326ea9-f651-42b3-bcea-29aa59ac3047', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', 'bec70501-53bd-49a8-bc48-c184c43cafd1', '600'),
('84d0f863-1c8d-4e77-9634-083179142622', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', 'e57e1ccd-9b1b-41e2-9c3d-828eb6b7a036', '0'),
('57ecb88f-caa1-4fc7-b684-77ad2da325d9', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', '6cf66d67-1e9d-44a5-8e7b-e7f1afaccf4c', '0'),
('ed098eda-9660-4455-b653-962720d4334f', 'a81d398b-9098-46ed-ac07-bb3407441e7f', '6033ffc7-948a-4528-9572-116614fa9a88', '100');

-- Preparation Method
INSERT INTO taco.preparation_method ("uuid", "dish_uuid", "preparation_method") VALUES ('3c8d0100-0a69-4181-9da2-0f8585835f19', '0c9be464-bf75-4a2b-8af8-f97d3747d580', '1. Ralar o alho na microplana\n2. Cortar a cebola em brunoise\n3. Separar o alho e a cebola em uma vasilha, junto de uma pitada de sal, adobo e manjerona\n4. Ralar o caldo knorr na microplana e reservar em um pilão\n6. Adicionar ao caldo knorr pimenta do reino, 50 ml de óleo vegetal, sal e MSG e macerar até emulsionar\n7. Cortar a salsa e reservar\n8. Cortar os cogumelos Portobello em fatias de 3 mm\n9. Cortar o peito de frango em cubos\n10. Misturar o tempero de caldo knorr ao frango e reservar\n11. Esquentar a panela com um fio fino de óleo\n12. Fritar o frango em duas partes, para dourar corretamente\n13. Retirar o frango e adicionar à panela os itens do passo 3\n14. Após refogar a cebola, adicionar os cogumelos e 2 tomates enlatados (não duas latas, dois tomates)\n15. Após secar quase toda a água dos cogumelos, adicionar o frango\n16. Após 2, desligar o fogo e adicionar o creme de leite com a salsa'),
('f072b02d-85dc-47f7-ac67-300e31f10a33', 'ab2f19a7-0c67-4e41-a257-abcaa28b4e99', '1. Marinate the diced chicken breast with 2 tablespoons of light soy sauce, 2 tablespoons of Shaoxing cooking wine (or Mirin), white pepper, and the egg white. Mix well and leave in the fridge for one hour.\n2. Fill a wok or large frying pan half full with oil and heat to around 180°C (350°F) for deep frying.\n3. In a bowl, mix together the cornflour, rice flour, and baking powder. Season with salt. Place some marinated chicken pieces into the flour mixture and coat well.\n4. Once the chicken is coated, carefully lower it into the hot oil and fry until golden brown and crispy, about 6 to 7 minutes. Remove from the oil and place onto a wire rack to drain.\n5. In a bowl, mix together 1 tablespoon of light soy sauce, 4 tablespoons of water, grated garlic, chicken bouillon, rice vinegar, and honey. Stir well until everything is dissolved.\n6. Once the chicken is fried, remove the oil from the wok and place it back on the heat. Add the sauce you just made and bring to a simmer.\n7. Once the sauce has been simmering for one to two minutes, add the chicken back to the wok and coat well in the honey sauce. Toss the chicken carefully to evenly coat in the sticky sauce.\n8. Place the chicken into your serving dish and garnish with some white sesame seeds and spring onions. Serve alongside steamed white rice.');
