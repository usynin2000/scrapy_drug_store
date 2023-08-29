from itemadapter import ItemAdapter


class AptekascraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # delete all unwanted elements from the list
        raw_section = adapter.get('section')
        adapter['section'] = [item.strip() for item in raw_section
                              if item.strip() != '']

        # take from string price and make it float
        price_data = adapter.get('price_data')
        if price_data:
            current = float(price_data.split('\n')[1].strip().split()[0])
            original = float(price_data.split('\n')[1].strip().split()[0])
            sale_tag = int((original / 100) * (original - current))
        else:
            current = 0
            original = 0
            sale_tag = "Cкидка 0 %"
        adapter['price_data'] = {
            'current': current,
            'original': original,
            'sale_tag': f'Скидка {sale_tag} %',
        }

        # give main info about stock and give quantaty
        stock = adapter.get('stock')
        if stock:
            in_stock = True
            count = int(stock.split(' ')[5])
        else:
            in_stock = False
            count = 0

        adapter['stock'] = {
            'in_stock': in_stock,
            'count': count,
        }

        # make dict of assets
        img_url = adapter.get('assets')
        if img_url:
            adapter['assets'] = {
                'main_image': img_url,
                "set_images": [],
                "view360": [],
                "video": [],
            }

        # make description as a string
        metadata_list = adapter.get('metadata')
        description_without_RNT = ([item
                                    .replace('\r', '')
                                    .replace('\n', '')
                                    .replace('\t', '')
                                    for item in metadata_list])
        description = ([item.strip() for item in description_without_RNT
                        if item.strip()])
        adapter['metadata'] = {
            '__description': ' '.join(description),
        }

        return item
