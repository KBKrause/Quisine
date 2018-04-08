package com.example.competition.quisine1;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.content.Intent;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;
import android.widget.ArrayAdapter;

import java.net.URL;
import java.util.ArrayList;

public class enter_ingredients extends AppCompatActivity {
 /**private Button b; **/
    String ingredient;
    EditText ingredientInput;
    Button save;
    ArrayList<String> addArray = new ArrayList<String>();
    EditText txt;
    ListView show;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_enter_ingredients);

        txt = (EditText)findViewById(R.id.txtInput);
        show = (ListView)findViewById(R.id.listView);
        save = (Button)findViewById(R.id.button_add);
        save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String getInput = txt.getText().toString();

                if (addArray.contains(getInput)) {
                    Toast.makeText(getBaseContext(), "Ingredient Already Added", Toast.LENGTH_LONG).show();
                } else if (getInput == null || getInput.trim().equals("")) {
                    Toast.makeText(getBaseContext(), "Input Field Is Empty", Toast.LENGTH_LONG).show();
                } else {
                    addArray.add(getInput);
                    ArrayAdapter<String> adapter = new ArrayAdapter<String>(enter_ingredients.this, android.R.layout.simple_list_item_1, addArray);
                    show.setAdapter(adapter);
                    ((EditText) findViewById(R.id.txtInput)).setText(" ");
                }
            }
        });

        /** URL url = new URL("https://google.com"); **/



        /**
        ingredientInput = (EditText) findViewById(R.id.ingredientInput);
        save = (Button) findViewById(R.id.button_add);

        b = (Button)findViewById(R.id.begin_button);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent( enter_ingredients.this,find_a_recipe.class);
                startActivity(i);
            }

        });  **/

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ingredient = ingredientInput.getText().toString();
                showToast(ingredient);

                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
    }

    private void showToast(String text) {
        Toast.makeText(enter_ingredients.this, text, Toast.LENGTH_SHORT).show();
    }

}
