Monarch DTA v1
Monarch DT      https://www.servicetitan.com
App ID   :      9jxbbcf06a42i
Tenant ID:      1270943139
Client ID:      cid.dtq2ekk9l23mnp70y3sowky89
Client Secrect: cs2.yk71kq7hj0xyi3x5bd1syl0xazjxm344crle3mkxvripg0m80g

Monarch FA v1
Monarch DT      https://www.servicetitan.com/
App ID        : 616t4rxryyfjz
Tenant ID     : 1270943139
Client ID     : cid.fro8hb6ts6mhbfjwl7yes04qc		
Client Secrect: cs1.d37td4ghf8c2ctq3vyitua2s8ffpkpa1k2w3q2ym7m3mlitmx9

prueba
Monarch DT      https://www.servicetitan.com/
App ID        : uayv62ftxhlt4
Tenant ID     : 1270943139
Client ID     : cid.l0sg3fc0a50mhz8at28y0rue6
Client Secrect: cs1.elvglv8668rpw8efeoqe4wmj2baxcai6fly0pl4b17rmk7voxu



echo -n "9jxbbcf06a42i" | gcloud secrets create ST_APP_ID --data-file=-
echo -n "cid.dtq2ekk9l23mnp70y3sowky89" | gcloud secrets create ST_CLIENT_ID --data-file=-
echo -n "cs2.yk71kq7hj0xyi3x5bd1syl0xazjxm344crle3mkxvripg0m80g" | gcloud secrets create ST_CLIENT_SECRET --data-file=-
echo -n "1270943139" | gcloud secrets create ST_TENANT_ID --data-file=-








    